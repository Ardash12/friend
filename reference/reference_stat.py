from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from reference.schemas import BasicRegister
from . import service


router = APIRouter()

@router.get('v1/user/{id}', response_model=List[BasicRegister])
def ref_list(db: Session = Depends(get_db)):
    return service.get_reference_list(db)


@router.post('/')
def ref_list(item: BasicRegister, db: Session = Depends(get_db)):
    return service.post_reference(db, item)
