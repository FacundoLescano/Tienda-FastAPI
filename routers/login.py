from fastapi import APIRouter
from pydantic import BaseModel
from db.mongo import consult, insert

router = APIRouter()

class User(BaseModel):
    id: int
    username: str
    password: str


@router.post("/sign-up", tags=["sign-up"])
def sign_up(user: User):
    x = insert("users", dict(user))
    return user


@router.post("/login", tags=["login"])
def login(user: User):

    for i in users:
        if i["username"] == user.username and i["password"] == user.password:
            return i["id"]

    return "incorrecto"


@router.delete("/delete-user", tags=["delete-user"])
def delete_user():

    pass