from fastapi import APIRouter, HTTPException
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, UserSchema, PremiumRequest, UpdateUser
import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_user(_user: UserSchema, db: Session = Depends(get_db)):
    crud.create_user(db, user=_user)
    return Response(status="OK",
                    code="201",
                    message="User created successfully").dict(exclude_none=True)


@router.get("/")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _users = crud.get_users(db, skip, limit)
    return _users


@router.get("/{_id}")
async def get_by_id(_id: int, db: Session = Depends(get_db)):
    _user = crud.get_user_by_id(db, _id)
    if _user is None:
        raise HTTPException(status_code=404, detail=f"User with id: {_id} does not exists")
    return _user


@router.patch("/{_id}")
async def update_user(_id: int, _user: UpdateUser, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, _id)
    if user is None:
        raise HTTPException(status_code=404, detail=f"User with id: {_id} does not exists")

    _user = crud.update_user(db, _user, _id)
    return Response(status="OK", code="200", message="Success update data", result=_user)


@router.patch("/{_id}/premium")
async def update_premium_status(_id: int, request: PremiumRequest, db: Session = Depends(get_db)):
    _user = crud.get_user_by_id(db, _id)
    if _user is None:
        raise HTTPException(status_code=404, detail=f"User with id: {_id} does not exists")

    _user = crud.update_premium_status(db, user_id=_id, premium=request.premium)
    return Response(status="OK", code="200", message="Premium status updated", result=_user)


@router.delete("/{_id}")
async def delete_user(_id: int, db: Session = Depends(get_db)):

    _user = crud.get_user_by_id(db, _id)
    if _user is None:
        raise HTTPException(status_code=404, detail=f"User with id: {_id} does not exists")

    crud.remove_user(db, user_id=_id)
    return Response(status="OK", code="204", message="Success deleted data").dict(exclude_none=True)
