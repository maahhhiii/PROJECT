# Silicon Campus Hub - Project Documentation

## 1. Team Member Details

| Name         | Silicon ID   | Email Address              |
|--------------|--------------|----------------------------|
| Mahi         | 24BCSF72     | cse.24bcsf72@silicon.ac.in |


## 2. What Has Been Done and How

The *Silicon Campus Hub* is a backend web application built using *FastAPI* to manage essential student services. It provides three core features: User Management, Announcements, and Lost & Found.

## 1. User Management Module

*What was done*:
- Created signup/login API routes.
- Implemented role-based access and JWT authentication.

*How*:
- Used FastAPI to create secure endpoints.
- Used passlib for password hashing and python-jose for JWT token generation.
- Role-based access was handled through custom FastAPI dependencies.

## 2. Announcement Module

*What was done*:
- Created APIs for admin users to post, update, delete announcements.
- Created endpoints for students to view announcements.

*How*:
- Used SQLAlchemy to define models and interact with the SQLite database.
- FastAPI routes were created for CRUD operations.
- Authentication used to restrict certain actions to admin users only.

## 3. Lost & Found Module

*What was done*:
- Built APIs to post and search for lost or found items.
- Allowed users to perform all CRUD operations on their items.

*How*:
- Created database models using SQLAlchemy.
- Validated data with Pydantic schemas.
- Integrated JWT authentication to protect endpoints.

## Other Components

- .env file was used to manage secrets and configuration.
- utils.py file used for helper functions like token validation.
- Used Git and GitHub for version control and project tracking.

## 3. Roles and Responsibilities

Since this was an individual project, all roles and tasks were handled by MAHI [24BCSF72].

| Role               | Responsibility Description                                                                  |
|--------------------|---------------------------------------------------------------------------------------------|
| Backend Developer  | Built all FastAPI endpoints, designed database models, and wrote business logic.            |
| Auth & Security    | Implemented JWT authentication and role-based access control.                               |
| Database Designer  | Defined and managed SQLite models using SQLAlchemy ORM.                                     |
| Tester             | Used Postman to test all routes and handled bug fixing.                                     |
| Documentation Lead | Created this documentation and maintained project structure on GitHub.                      |

## 4. API Preview - Swagger UI

Below is the preview of working APIs exposed through Swagger UI (http://127.0.0.1:8000/docs):

## Available Endpoints:

## User Authentication
- POST /register – Register a new user
- POST /login – User login with JWT token

## Announcements
- POST /announcements – Post announcement (admin only)
- GET /announcements – Get all announcements
- GET /announcements/{id} – Get one announcement
- DELETE /announcements/{id} – Delete announcement (admin only)

## Lost & Found
- POST /lost-found – Create lost/found item
- GET /lost-found – Get all lost/found items
- GET /lost-found/{id} – Get a specific item
- PUT /lost-found/{id} – Update a lost/found item
- DELETE /lost-found/{id} – Delete an item
- POST /lost-found/upload – Upload image/file

## 5. Notes

- All API endpoints tested using Swagger UI and Postman.
- Proper status codes and validation error handling implemented.

STATUS: Project successfully completed and deployed to GitHub  
SUBMISSION DATE: [06/07/2025]