from sqlalchemy.orm import Session
from models import User
from schemas import UserSchema, UpdateUser


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: UserSchema):
    _user = User(**user.dict())
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


def remove_user(db: Session, user_id: int):
    _user = get_user_by_id(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()


def update_user(db: Session, user: UpdateUser, user_id: int):
    _user = get_user_by_id(db=db, user_id=user_id)

    if user.first_name is not None:
        _user.first_name = user.first_name
    if user.last_name is not None:
        _user.last_name = user.last_name
    if user.role is not None:
        _user.role = user.role
    if user.email is not None:
        _user.email = user.email
    if user.promotional is not None:
        _user.promotional = user.promotional
    if user.address is not None:
        _user.address = user.address
    if user.points is not None:
        _user.points = user.points

    db.commit()
    db.refresh(_user)
    return _user


def update_premium_status(db: Session, user_id: int, premium: bool):
    _user = get_user_by_id(db=db, user_id=user_id)

    _user.premium = premium

    db.commit()
    db.refresh(_user)
    return _user
