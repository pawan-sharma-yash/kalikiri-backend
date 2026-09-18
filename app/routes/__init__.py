"""
Legacy routes package.

Canonical routers live in `app.routers`. This package re-exports for compatibility.
"""

from app.routers.auth import router as auth_router  # noqa: F401

__all__ = ["auth_router"]
