from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from dependency import get_db
from auth import crud
from auth.schemas import UserCreate

router = APIRouter(
    prefix="/auth",
)


@router.post("/create-user")

def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = crud.create_user(db, user)
    return new_user