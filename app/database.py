"""
Backward compatibility shim.

`app` was previously defined here. Now canonical definition lives in `app.main`.
This module re-exports `app` so `from app.database import app` keeps working.
For new code, use `from app.main import app`.
"""

from app.main import app  # noqa: F401

# Re-export DB placeholder for structure compliance
try:
    from app.core.database import get_db  # noqa: F401
except ImportError:
    pass