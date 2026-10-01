from pydantic import BaseModel

#Objeto para productos
class Product(BaseModel):
    id: int
    nameP: str
    price: float
