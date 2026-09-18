from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response

from app.database import app
from app.models.auth import LoginRequest


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Streamline errors using Pydantic-native filtering when supported,
    # fallback to common logic otherwise (as requested).
    try:
        # Pydantic v2 supports include_* flags to reduce noise (input/url/context)
        # FastAPI's ValidationException.errors() doesn't accept args, so this will
        # raise TypeError -> fallback to manual filtering below.
        raw_errors = exc.errors(include_url=False, include_context=False, include_input=False)  # type: ignore[call-arg]
    except TypeError:
        # Common logic fallback: manually filter noisy fields (input, ctx, url, type, loc)
        raw_errors = exc.errors()

    messages = []
    for err in raw_errors:
        msg = err.get("msg", "")
        # Strip "Value error, " prefix added by Pydantic field_validator
        if msg.startswith("Value error, "):
            msg = msg[len("Value error, ") :]
        # For generic errors like "Field required", include field name for clarity
        loc = err.get("loc", [])
        if loc and len(loc) > 1 and "Field required" in msg:
            field = str(loc[-1])
            msg = f"{field}: {msg}"
        messages.append(msg)
    detail = messages[0] if len(messages) == 1 else "; ".join(messages)
    return JSONResponse(status_code=422, content={"detail": detail})


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)


@app.post("/login")
async def login(request: LoginRequest):
    # Pydantic validation already ensures email validity and password strength
    # In a real app, verify credentials against DB here
    return {"message": "Login successful", "email": request.email}
