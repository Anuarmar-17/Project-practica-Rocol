from pydantic import BaseModel

#Objetos para usuarios
class Usuario(BaseModel):
    id: int
    nombre: str
    apellido: str
    edad: int