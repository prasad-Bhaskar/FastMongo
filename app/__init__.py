"""
FastMongo — FastAPI + MongoDB example application

Package purpose
-----------------
This package contains a small example REST API built with FastAPI
and Motor (async MongoDB driver). It demonstrates:

- Project layout for a FastAPI application
- Centralized configuration using `app.core.config.Settings`
- Authentication-related routes in `app.auth`
- Database connection and index creation in `app.core.database`
- A common response contract in `app.utils.response`
- Custom application exceptions in `app.utils.exceptions`

Quick start
-----------
1. See the project `INSTALL.md` at the repository root for setup and
	Python version guidance.
2. Create and activate a Python 3.11 virtualenv and install
	dependencies from `requirements.txt`.
3. Create a `.env` file with required environment variables (see
	`app.core.config.Settings`).
4. Run the app:

	uvicorn app.main:app --reload

Notes for maintainers
---------------------
- Keep `app.main` as the application entrypoint.
- Prefer returning the project's `APIResponse` from routers so responses
  are consistent across endpoints.
- Use the `app.utils.exceptions.BaseAppException` subclasses to surface
  predictable application errors with proper status codes.

"""

__all__ = ["main"]

