from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response

from app.database import app
from app.models.auth import LoginRequest


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Reduce noise: return only human-readable messages instead of full pydantic error objects
    messages = []
    for err in exc.errors():
        msg = err.get("msg", "")
        # Strip "Value error, " prefix added by Pydantic
        if msg.startswith("Value error, "):
            msg = msg[len("Value error, ") :]
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
