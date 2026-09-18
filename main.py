"""
Root entry point for `uvicorn main:app --reload`.

Canonical app lives in `app.main`. This wrapper keeps backward compatibility
for existing run commands while proper structure lives under `app/`.

Deployable: `python main.py` now listens on 0.0.0.0:$PORT (Railpack/Panda stack
expects app to listen on 0.0.0.0 and $PORT, not 127.0.0.1 or hardcoded port).
"""

from app.main import app  # noqa: F401

__all__ = ["app"]

if __name__ == "__main__":
    import os

    import uvicorn

    port = int(os.getenv("PORT", "3000"))
    # Must listen on 0.0.0.0 for remote deployment (not 127.0.0.1)
    uvicorn.run(app, host="0.0.0.0", port=port)
