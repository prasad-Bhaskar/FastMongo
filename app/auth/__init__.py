"""
Authentication package
----------------------
Contains authentication-related routes, schemas and services used by the
application. Key modules:

- `router.py` - FastAPI routes for registration and login
- `service.py` - Business logic for registering and authenticating users
- `schemas.py` - Pydantic request/response models

Notes
- Return the project's `APIResponse` from routes to keep responses
	consistent.
"""

__all__ = ["router", "service", "schemas"]

