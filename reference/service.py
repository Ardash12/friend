from sqlalchemy.orm import Session
from .models import Users
from reference.schemas import BasicRegister, UserId


def get_reference_list(db: Session):

    return db.query(Users).all()
    # return db.query(Users).filter(Users.id == user_id)


def post_reference(db: Session, item: BasicRegister):
    """Записываем в БД данные из post запроса"""

    ref = Users(**item.dict())
    db.add(ref)
    db.commit()
    db.refresh(ref)
    return ref

