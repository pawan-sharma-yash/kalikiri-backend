from fastapi import APIRouter

from app.schemas.auth import LoginRequest

router = APIRouter(tags=["auth"])


@router.post("/login")
async def login(request: LoginRequest):
    # Pydantic validation already ensures email validity and password strength
    # In a real app, verify credentials against DB here
    return {"message": "Login successful", "email": request.email}
