from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from .. import models, schemas, database, auth

router = APIRouter(prefix="/book", tags=["Bookings"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    payload = auth.decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(models.User).filter(models.User.email == payload.get("sub")).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/")
def book_class(data: schemas.BookingCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    fitness_class = db.query(models.FitnessClass).filter(models.FitnessClass.id == data.class_id).first()
    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")
    if fitness_class.availableSlots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")
    fitness_class.availableSlots -= 1
    booking = models.Booking(**data.dict(), user_id=current_user.id)
    db.add(booking)
    db.commit()
    return {"message": "Booking successful"}

@router.get("/")
def my_bookings(db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Booking).filter(models.Booking.user_id == current_user.id).all()
