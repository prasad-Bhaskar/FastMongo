"""
Core utilities and configuration for the application.

Key modules:

- `config.py` - Pydantic settings and environment handling
- `database.py` - Motor client and helper to create indexes
- `exception_handler.py` - Global exception handling utilities
- `response_middleware.py` - Optional response middleware (not enabled by default)
- `security.py` - Helpers for password hashing and token creation

This package contains shared infrastructure code used across the app.
"""

__all__ = ["config", "database", "exception_handler", "security"]

