from sqlalchemy import Column, String, Integer, DateTime, Date
from core.db import Base


class Reference(Base):
    """Модели для создания таблицы в БД"""

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    phone = Column(String)
    login = Column(String)
    name = Column(String)
    password = Column(String)
    birth = Column(Date)
    tg = Column(String)
    email = Column(String, unique=True, index=True)
