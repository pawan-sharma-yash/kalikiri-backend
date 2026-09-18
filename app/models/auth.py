import re

from pydantic import BaseModel, ConfigDict, field_validator


class LoginRequest(BaseModel):
    model_config = ConfigDict(
        hide_input_in_errors=True,
        # Pydantic-native way to reduce noise: hides `input` field from errors
        # url/context also filtered in handler via errors(include_...=False) when supported
    )

    email: str
    password: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str) -> str:
        # Use regex to avoid requiring `email-validator` extra dependency
        # Pydantic's EmailStr needs `email-validator` which is not installed
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_pattern, v):
            raise ValueError("Invalid email address")
        return v

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        # Strong password: min 8 chars, at least one uppercase, one lowercase, one digit, one special char
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"[0-9]", v):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-\\/\[\];'`~+=]", v):
            raise ValueError("Password must contain at least one special character")
        return v
