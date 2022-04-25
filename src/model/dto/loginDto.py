from pydantic import BaseModel
from typing import Optional


class LoginDto(BaseModel):
    login: str
    password: str
    activated: Optional[bool]
