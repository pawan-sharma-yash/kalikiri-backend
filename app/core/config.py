from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Kalikiri Backend"
    version: str = "1.0.0"
    debug: bool = False


settings = Settings()
