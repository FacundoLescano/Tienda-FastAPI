from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id: int
    username: str
    password: str

users = [
    {
        "id": 1,
        "username": "facundo",
        "password": "123"
    }
]

@router.post("/sign-up", tags=["sign-up"])
def sign_up(user: User):

    users.append(user)

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