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
.
├── backend
│   ├── alembic
│   │   ├── script.py.mako
│   │   └── versions
│   │       ├── 0320e6f57d5a_create_initial_tables.py
│   │       ├── 16aa7df35a39_add_is_verified_to_user_and_add_email_.py
│   │       ├── 820ac6683106_rename_password_to_hashed_password.py
│   │       ├── 93e8e9fc24d3_ajout_du_champ_is_verified_a_la_table_.py
│   ├── alembic.ini
│   ├── app
│   │   ├── core
│   │   │   ├── config.py   
│   │   │   ├── __init__.py
│   │   ├── crud
│   │   │   ├── auth.py
│   │   │   └── __init__.py
│   │   ├── db
│   │   │   ├── database.py
│   │   │   ├── __init__.py
│   │   │   └── security.py
│   │   ├── dependencies.py
│   │   ├── enums
│   │   │   ├── __init__.py
│   │   │   └── role_enum.py
│   │   ├── __init__.py
│   │   ├── internal
│   │   │   └── __init__.py
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── academic_year.py
│   │   │   ├── application.py
│   │   │   ├── domaine.py
│   │   │   ├── email_verification.py
│   │   │   ├── __init__.py
│   │   │   ├── programme.py
│   │   │   ├── role.py
│   │   │   ├── user.py
│   │   │   └── user_role.py
│   │   ├── routers
│   │   │   ├── auth.py
│   │   │   ├── __init__.py
│   │   ├── schemas
│   │   │   ├── __init__.py
│   │   │   ├── message.py
│   │   │   ├── token.py
│   │   │   └── user.py
│   │   ├── services
│   │   │   ├── email_service.py
│   │   │   ├── __init__.py
│   │   └── templates
│   │       ├── layout.html
│   │       └── static
│   │           ├── css
│   │           │   └── base.css
│   │           └── javascript
│   ├── poetry.lock
│   ├── pyproject.toml
│   ├── run.sh
│   ├── scripts
│   │   └── seed_roles.py
│   └── tests
├── docs
│   └── uml
│       └── enrollix_version1.uml
├── LICENSE
└── README.md
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
chmod +x ./scripts/run_backend.sh
./scripts/run_backend.sh
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

[GNU AFFERO GENERAL PUBLIC LICENSE](LICENSE)

---

## Author

[![Trésor](https://img.shields.io)](https://github.com)
