# Recipe Sharer

## Description
**Recipe Sharer** is a full-stack web application designed to demonstrate API functionality and automated testing using **FastAPI** and **pytest**.  
The project allows users to **create, view, and manage recipes**, with a lightweight **React** frontend and a **FastAPI** backend connected to an **SQLite** database.  

The main objective of this project is to implement **reliable API testing** to ensure the stability and accuracy of recipe-related operations such as creation, retrieval, and validation.

---

## Tools and Technologies Used
- **FastAPI** – Backend framework for building and testing REST APIs  
- **SQLite** – Lightweight database for storing and retrieving recipes  
- **React.js** – Frontend library for basic UI interaction  
- **Axios** – For communication between frontend and backend APIs  
- **Pytest** – Framework for automated backend testing, validation, and response verification  

---

## Basic Workflow

### Backend (FastAPI)
- Implements endpoints for recipe creation, retrieval, update, and deletion.  
- Returns structured JSON responses for frontend and testing validation.  
- Uses SQLite for persistent and lightweight data storage.

### Testing (Pytest)
- Focuses on backend validation and automated API testing.  
- Verifies recipe creation and data retrieval through endpoint tests.  
- Ensures consistent response formats, correct HTTP status codes, and data integrity.  

### Frontend (React)
- Provides a minimal interface to submit and view recipes.  
- Communicates with backend APIs using Axios for testing frontend-backend integration.

---

**Purpose:**  
This project emphasizes **API reliability through automated testing** and provides a foundation for extending test coverage across full-stack applications.
