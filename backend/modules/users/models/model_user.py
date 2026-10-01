from pydantic import BaseModel

#Objetos para usuarios
class User(BaseModel):
    id: int
    name: str
    lastname: str
    age: int