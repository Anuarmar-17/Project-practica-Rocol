from fastapi import APIRouter
from typing import Optional
from modules.users.models.model_user import User

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


#Variable usurio | db falsa
User_list = [User(id=1, name="Anaur", lastname="Martínez", age=23),
                   User(id=2, name="Ana", lastname="Lozano", age=23),
                   User(id=3, name="Carlos", lastname="Vegas", age=30)]

#Retorna todos los usuarios y por id | Query
@router.get("/")
async def users(id: Optional[int] = None):
    if id is not None:
        return search_user(id)

    return User_list

#Retorna un usuario por id | PATH
@router.get("/{id}")
async def user(id: int):
    return search_user(id)

#Función crear usuario
@router.post("/")
async def new_user(new_user: User):
    if type(search_user(new_user.id)) == User:
        return {"error": "El usuario ya existe"}
    else:
        User_list.append(new_user)
        return new_user

#Función buscar usuario
def search_user(id: int):
    user = filter(lambda user: user.id == id, User_list)
    try:
        return list(user)[0]
    except:
        return {"error": "El usuario no fue encontrado"}
