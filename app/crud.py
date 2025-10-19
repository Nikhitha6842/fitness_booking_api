from sqlalchemy.orm import Session
from . import models, schemas, auth
from datetime import datetime

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.hash_password(user.password)
    db_user = models.User(name=user.name, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_class(db: Session, fitness_class: schemas.ClassCreate):
    db_class = models.FitnessClass(
        name=fitness_class.name,
        dateTime=fitness_class.dateTime,
        instructor=fitness_class.instructor,
        availableSlots=fitness_class.availableSlots
    )
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

def get_all_classes(db: Session):
    return db.query(models.FitnessClass).filter(models.FitnessClass.dateTime >= datetime.utcnow()).all()

# Booking CRUD
def book_class(db: Session, booking: schemas.BookingCreate, user_id: int):
    fitness_class = db.query(models.FitnessClass).filter(models.FitnessClass.id == booking.class_id).first()
    if not fitness_class:
        return None, "Class not found"
    if fitness_class.availableSlots <= 0:
        return None, "No slots available"

    fitness_class.availableSlots -= 1
    db_booking = models.Booking(
        user_id=user_id,
        class_id=booking.class_id,
        client_name=booking.client_name,
        client_email=booking.client_email
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking, None

def get_user_bookings(db: Session, user_id: int):
    return db.query(models.Booking).filter(models.Booking.user_id == user_id).all()
