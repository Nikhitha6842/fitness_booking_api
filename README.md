# Fitness Booking API

A backend API for a fictional **fitness studio** that allows users to view and manage fitness classes. Implemented using **FastAPI**, **SQLite**, and **SQLAlchemy**, with **JWT-based authentication** for secure access.

---

## Table of Contents

- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Project Structure](#project-structure)  
- [Setup Instructions](#setup-instructions)  
- [API Endpoints](#api-endpoints)  
- [Notes](#notes)  
- [Author](#author)  

---

## Features

### User Authentication

- **Sign up** (`POST /user/signup`) with name, email, and password  
- **Login** (`POST /user/login`) to receive a JWT token  
- Passwords are securely hashed using **bcrypt**  
- Only authenticated users can create classes, book classes, or view bookings  

### Class Management

- **Create a new fitness class** (`POST /classes`) with:  
  - Class name  
  - Date & time  
  - Instructor  
  - Available slots  
- **Fetch all upcoming fitness classes** (`GET /classes`)  
- All class actions require authentication  

### Booking Management

- **Book a class** (`POST /book`) with client name and email  
- Validates available slots and prevents overbooking  
- Deducts slots automatically after successful booking  
- **View all bookings** of the logged-in user (`GET /bookings`)  

### Database

- Uses **SQLite (`fitness.db`)** for storing users, classes, and bookings  
- Models are implemented with **SQLAlchemy ORM**  
- Automatic table creation on application startup  

### API Documentation

- Swagger UI available at `/docs`  
- Interactive testing for all endpoints  

### Security & Error Handling

- JWT token expiration: **30 minutes**  
- Handles invalid credentials, unauthorized access, missing fields, and overbooking errors  

---

## Tech Stack

- Python 3.12+  
- FastAPI  
- SQLAlchemy  
- SQLite  
- Passlib (for password hashing)  
- Python-JOSE (for JWT handling)  
- Pydantic (data validation)  

---

## Project Structure

```text
fitness_booking_api/
├─ main.py              # FastAPI app initialization
├─ database.py          # Database configuration and session
├─ models.py            # SQLAlchemy models (User, Class, Booking)
├─ schemas.py           # Pydantic request/response schemas
├─ crud.py              # CRUD helper functions
├─ auth.py              # JWT authentication and password hashing
└─ routes/
   ├─ users.py          # User signup and login endpoints
   ├─ classes.py        # Fitness class endpoints
   └─ bookings.py       # Booking endpoints

##Setup Instructions

1. **Clone the Repository**
git clone https://github.com/Nikhitha6842/Fitness_Booking_API
cd fitness_booking_api

2. **Create Virtual Environment**
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. **Install dependencies**
pip install -r requirements.txt

4. **Run the application**
uvicorn main:app --reload
Server runs at: http://127.0.0.1:8000
Swagger UI: http://127.0.0.1:8000/docs

**API Endpoints**

| Endpoint       | Method | Description                            |
| -------------- | ------ | -------------------------------------- |
| `/user/signup` | POST   | Register a new user                    |
| `/user/login`  | POST   | Login and get JWT token                |
| `/classes`     | POST   | Create a new class (auth required)     |
| `/classes`     | GET    | Get all upcoming classes               |
| `/book`        | POST   | Book a class (auth required)           |
| `/book`        | GET    | Get all bookings of the logged-in user |


Notes

All endpoints are tested and functional using Swagger UI
Authentication is required for creating classes, booking classes, and viewing bookings
Times are stored in UTC internally; timezone conversion can be added if needed
Project is modular and easy to extend for future features

Author
Gulla Nikhitha – Fitness Booking API implementation for  assignment.