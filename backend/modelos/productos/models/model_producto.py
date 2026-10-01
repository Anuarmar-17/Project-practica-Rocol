from pydantic import BaseModel

#Objeto para productos
class Producto(BaseModel):
    id: int
    nombreP: str
    precio: float
