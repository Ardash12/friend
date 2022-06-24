from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from reference.schemas import BasicRegister, UserId
from .models import Users
from . import service


router = APIRouter()

@router.get('/v1/user/{', response_model=List[BasicRegister])
def ref_list(user_id: int, db: Session = Depends(get_db)):
    result = db.query(Users).filter(Users.id == user_id).all()
    print(result)
    return result

# @router.get('v1/user/{id}')
# def ref_list(user_id=id, db: Session = Depends(get_db)):
#     return service.get_reference_list(db, user_id)


@router.post('v1/auth/register/')
def ref_list(item: BasicRegister, db: Session = Depends(get_db)):
    return service.post_reference(db, item)
