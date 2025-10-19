from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime

from .. import models, schemas, database, auth

router = APIRouter(prefix="/classes", tags=["Classes"])

# OAuth2 scheme (connects to /user/login)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

# get current loged-in user

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    payload = auth.decode_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    email = payload.get("sub")
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

#create new classes

@router.post("/")
def create_class(
    fitness_class: schemas.FitnessClassCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    new_class = models.FitnessClass(**fitness_class.dict())
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return {
        "message": "Class created successfully",
        "class": new_class
    }

# get all upcoming classes

@router.get("/")
def get_classes(db: Session = Depends(database.get_db)):
    upcoming = db.query(models.FitnessClass).filter(
        models.FitnessClass.dateTime > datetime.utcnow()
    ).all()
    return upcoming
