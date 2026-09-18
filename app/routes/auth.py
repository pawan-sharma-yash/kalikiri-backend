"""
Backward compatibility shim for `app.routes.auth`.

Canonical router lives in `app.routers.auth`.
"""

from app.routers.auth import router  # noqa: F401
from app.routers.auth import login  # noqa: F401

__all__ = ["router", "login"]
