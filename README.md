# Fitness Booking API

A backend API for a fictional fitness studio that allows users to view and manage fitness classes. This project is implemented using **FastAPI**, **SQLite**, and **SQLAlchemy**, and uses **JWT-based authentication** for secure access.

---

## **Features Implemented**

1. **User Authentication**
   - Sign up (`POST /user/signup`) with name, email, and password.
   - Login (`POST /user/login`) and receive a JWT token.
   - Passwords are securely hashed using `bcrypt`.
   - Only authenticated users can create classes, book classes, or view their bookings.

2. **Class Management**
   - Create a new fitness class (`POST /classes`) with:
     - Class name
     - Date & time
     - Instructor
     - Available slots
   - Fetch all upcoming fitness classes (`GET /classes`).
   - All class-related actions require authentication.

3. **Booking Management**
   - Book a class (`POST /book`) with client name and email.
   - Validates available slots and prevents overbooking.
   - Deducts available slots automatically after booking.
   - View all bookings of the logged-in user (`GET /bookings`).

4. **Database**
   - Uses **SQLite** (`fitness.db`) for storing users, classes, and bookings.
   - Database models use SQLAlchemy ORM with proper relationships.
   - Automatic table creation on application startup.

5. **API Documentation**
   - Fully documented via **Swagger UI**.
   - Accessible at `/docs` when the server is running.
   - Provides request/response examples for all endpoints.

6. **Security**
   - JWT token expiration implemented (30 minutes).
   - Protected endpoints require valid token.
   - Handles invalid credentials and unauthorized access.

7. **Error Handling**
   - Missing fields return HTTP 422 errors.
   - Overbooking attempts return HTTP 400.
   - Invalid authentication returns HTTP 401.

---

## **Optional / Bonus Features**
- Unit tests: Not implemented (optional)
- Logging: Not implemented (optional)
- Token refresh: Not implemented (optional)
> These can be added for enhanced functionality.

---

## **Tech Stack**
- Python 3.12+
- FastAPI
- SQLAlchemy
- SQLite
- Passlib (for password hashing)
- Python-JOSE (for JWT handling)
- Pydantic (data validation)

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd fitness_booking_api

2. **Create Virtual Environment**
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. **Install dependencies**
pip install -r requirements.txt

4. **Run the application**
uvicorn main:app --reload
The server will start at http://127.0.0.1:8000.

5. **Access API Documentation**
Open your browser and navigate to:
http://127.0.0.1:8000/docs
Here, you can test all endpoints interactively.

**API Endpoints**

| Endpoint       | Method | Description                            |
| -------------- | ------ | -------------------------------------- |
| `/user/signup` | POST   | Register a new user                    |
| `/user/login`  | POST   | Login and get JWT token                |
| `/classes`     | POST   | Create a new class (auth required)     |
| `/classes`     | GET    | Get all upcoming classes               |
| `/book`        | POST   | Book a class (auth required)           |
| `/book`        | GET    | Get all bookings of the logged-in user |

**Project Structure**  

fitness_booking_api/
│
├─ main.py              # FastAPI app initialization
├─ database.py          # Database configuration and session
├─ models.py            # SQLAlchemy models (User, Class, Booking)
├─ schemas.py           # Pydantic request/response schemas
├─ crud.py              # CRUD helper functions
├─ auth.py              # JWT authentication and password hashing
└─ routes/
    ├─ users.py         # User signup and login endpoints
    ├─ classes.py       # Fitness class endpoints
    └─ bookings.py      # Booking endpoints

Notes

All endpoints are tested and functional using Swagger UI.
Authentication is required for creating classes, booking classes, and viewing bookings.
Times are stored in UTC internally; you may add timezone conversion if needed.
The project is modular and easy to extend for future features.

Author
Gulla Nikhitha – Fitness Booking API implementation for  assignment.