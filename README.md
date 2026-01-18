# ENROLLIX

## Overview

This application is a **role-based university management platform** built with **FastAPI**, **SQLAlchemy**, and **Alembic**. It provides a solid backend foundation for managing users, authentication, authorization (RBAC), and academic entities in a scalable and production-ready manner.

The project is designed with **clean architecture**, **security best practices**, and **future extensibility** in mind.

---

## Core Features

* User registration with **email verification**
* Secure authentication using **JWT (OAuth2 Password Flow)**
* **Role-Based Access Control (RBAC)**
* Background tasks for email delivery
* Database migrations with **Alembic**
* Server-side HTML email templates with **Jinja2**
* Modular and maintainable project structure

---

## User Roles

The system supports multiple user roles using an Enum-based RBAC strategy:

* **SUPER_ADMIN** – Full system control
* **UNIVERSITY_ADMIN** – Manages a university and its resources
* **STUDENT** – Standard user with limited access

Access to protected endpoints is enforced via role-based dependencies.

---

## Technology Stack

| Layer            | Technology              |
| ---------------- | ----------------------- |
| API              | FastAPI                 |
| ORM              | SQLAlchemy              |
| Auth             | OAuth2 + JWT            |
| Password Hashing | argon2-cffi             |
| Migrations       | Alembic                 |
| Database         | PostgreSQL              |
| Background Tasks | FastAPI BackgroundTasks |
| Templating       | Jinja2                  |
| Email            | SMTP (planned)          |

---

## Project Structure

```text
.
├── backend
│   ├── alembic
│   │   ├── env.py
│   │   └── versions
│   ├── alembic.ini
│   ├── app
│   │   ├── core
│   │   ├── db
│   │   ├── enums
│   │   ├── models
│   │   ├── routers
│   │   ├── schemas
│   │   ├── services
│   │   ├── templates
│   │   │   ├── layout.html
│   │   │   └── static
│   │   │       ├── css
│   │   │       └── javascript
│   │   └── main.py
│   ├── run.sh
│   └── tests
└── docs
    └── uml
```

---

## Templating & Email Rendering (Jinja2)

This project uses **Jinja2** to render server-side HTML templates, primarily for transactional emails such as:

* Email verification
* Account-related notifications (future)

Templates are located in `app/templates/` and can include static assets (CSS/JS) for richer email rendering.

Example use case:

* Generate a verification email with a secure token
* Render HTML using Jinja2
* Send the email asynchronously via a background task

This approach ensures **maintainable, reusable, and well-formatted email content**.

---

## Authentication Flow

1. User registers with email and password
2. Password is hashed using **Argon2**
3. A verification token is generated
4. Verification email is rendered with **Jinja2** and sent asynchronously
5. User confirms email via verification endpoint
6. User can authenticate and receive a JWT access token

---

## RBAC (Role-Based Access Control)

Roles are enforced using FastAPI dependencies.

Example:

```python
@router.get("/admin-only")
def admin_route(
    user=Depends(require_role(Role.SUPER_ADMIN))
):
    return {"status": "authorized"}
```

This ensures strict separation of permissions across the platform.

---

## Database Migrations

Alembic is used for schema migrations.

* Migration scripts are stored in `alembic/versions/`
* Configuration is defined in `alembic.ini`
* Models metadata is loaded via `app.db.database.Base`

### Create a migration

```bash
alembic revision --autogenerate -m "add email verification"
```

### Apply migrations

```bash
alembic upgrade head
```

A helper script or Makefile can be used to simplify this workflow.

---

## Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql+psycopg2://user:password@localhost/dbname
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Email configuration
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=your-email
SMTP_PASSWORD=your-password
```

---

## Running the Application

### Development

```bash
chmod +x run.sh
./run.sh
```

or

```bash
uvicorn app.main:app --reload
```

### Production (example)

```bash
gunicorn -k uvicorn.workers.UvicornWorker app.main:app
```

---

## Security Considerations

* Passwords are never stored in plain text
* JWT tokens are signed and time-limited
* Email verification is required before activation
* Role-based permissions protect sensitive endpoints

---

## Roadmap

* Refresh tokens
* Password reset via email
* University and course management
* Audit logs
* Rate limiting

---

## Deployment (Planned)

- AWS EC2 for FastAPI deployment
- AWS RDS (PostgreSQL)
- AWS SES for transactional emails
- AWS S3 for file storage

---

## License

This project is provided for educational and professional use.

---

## Author

**Trésor Adzanto**
Computer Engineering Student 
