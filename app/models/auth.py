"""
Re-export for backward compatibility.

Canonical schema lives in `app.schemas.auth`.
Existing imports `from app.models.auth import LoginRequest` keep working.
"""

from app.schemas.auth import LoginRequest  # noqa: F401

__all__ = ["LoginRequest"]
