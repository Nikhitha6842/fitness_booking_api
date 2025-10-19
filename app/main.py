from fastapi import FastAPI
from .routes import users, classes, bookings
from . import models, database

app = FastAPI(title="Fitness Booking API")

models.Base.metadata.create_all(bind=database.engine)

# Include routes
app.include_router(users.router)
app.include_router(classes.router)
app.include_router(bookings.router)
