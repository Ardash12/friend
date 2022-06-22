from sqlalchemy import Column, String, Integer, DateTime, Date
from core.db import Base


class Reference(Base):
    """Модели для создания таблицы в БД"""

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    phone = Column(String)   # сделать обязательным полем
    login = Column(String)   # сделать обязательным полем
    name = Column(String)   # сделать обязательным полем
    password = Column(String)   # сделать обязательным полем
    birth = Column(Date)   # сделать обязательным полем
    tg = Column(String)
    email = Column(String, unique=True, index=True)




    user_id = Column(Integer)
    event_id = Column(Integer)
    event_type = Column(String)
    date = Column(DateTime)
