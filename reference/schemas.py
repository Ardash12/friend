from pydantic import BaseModel
from datetime import date


class UserId(BaseModel):
    name: str

    class Config:
        orm_mode = True


class BasicRegister(BaseModel):
    """Схема регистрации пользователя"""

    id: int
    phone: str
    login: str
    name: str
    password: str
    birth: date
    tg: str
    email: str

    class Config:
        orm_mode = True


# class ReferenceList(ReferenceBase):
#     """Схема для GET запросов"""
#
#     id: int
#
#
# class CreateReference(ReferenceBase):
#     """Схема для POST запросов"""
#
#     pass
