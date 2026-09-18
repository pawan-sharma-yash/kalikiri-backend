"""
Root entry point for `uvicorn main:app --reload`.

Canonical app lives in `app.main`. This wrapper keeps backward compatibility
for existing run commands while proper structure lives under `app/`.
"""

from app.main import app  # noqa: F401

__all__ = ["app"]
