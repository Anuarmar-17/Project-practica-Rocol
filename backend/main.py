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
    nombreP: str
    precio: float

#Variable producto
Lista_productos = [Producto(nombreP="Pizza", precio="60000"), 
                    Producto(nombreP="Hamburguesa", precio="50000"),
                    Producto(nombreP="Pasta", precio="45000")]

@app.get("/productos")
async def productos():
    return Lista_productos