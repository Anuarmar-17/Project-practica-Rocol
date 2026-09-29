from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root ():
    return "Prueba"

@app.get("/admin")
async def admin():
    return { "admin": "Anuar"}

#Objeto
class Producto(BaseModel):
    id: int
    nombreP: str
    precio: float

#Variable producto
Lista_productos = [Producto(id=1, nombreP="Pizza", precio="60000"), 
                    Producto(id=2, nombreP="Hamburguesa", precio="50000"),
                    Producto(id=3, nombreP="Pasta", precio="45000")]

#Retorna todos los productos
@app.get("/productos")
async def productos():
    return Lista_productos


#Retorna un producto por id | PATH
@app.get("/producto/{id}")
async def producto(id: int):
    producto = filter(lambda producto: producto.id == id, Lista_productos)
    try:
        return list(producto)[0]
    except:
        return { "error": "El producto no ha sido encontrado"}


#Retorna un producto por id | Query
@app.get("/productoquery/")
async def producto(id: int):
    producto = filter(lambda producto: producto.id == id, Lista_productos)
    try:
        return list(producto)[0]
    except:
        return { "error": "El producto no ha sido encontrado"}