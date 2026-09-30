from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root ():
    return "Prueba"

@app.get("/admin")
async def admin():
    return { "admin": "Anuar"}

#Objeto para productos
class Producto(BaseModel):
    id: int
    nombreP: str
    precio: float

#Objetos para usuarios
class Usuario(BaseModel):
    id: int
    nombre: str
    apellido: str
    edad: int


#Variable producto | db falsa
Lista_productos = [Producto(id=1, nombreP="Pizza", precio="60000"), 
                    Producto(id=2, nombreP="Hamburguesa", precio="50000"),
                    Producto(id=3, nombreP="Pasta", precio="45000")]

#Variable usurio | db falsa
Lista_usuarios = [Usuario(id=1, nombre="Anaur", apellido="Martínez", edad=23),
                   Usuario(id=2, nombre="Ana", apellido="Lozano", edad=23),
                   Usuario(id=3, nombre="Carlos", apellido="Vegas", edad=30)]

#Retorna todos los usuarios
@app.get("/usuarios")
async def usuarios():
    return Lista_usuarios

#Retorna todos los productos
@app.get("/productos")
async def productos():
    return Lista_productos


#Retorna un producto por id | PATH
@app.get("/producto/{id}")
async def producto(id: int):
    return buscar_producto(id)


#Retorna un producto por id | Query
@app.get("/productoquery/")
async def producto(id: int):
    return buscar_producto(id)

#Función buscar producto
def buscar_producto(id: int):
    producto = filter(lambda producto: producto.id == id, Lista_productos)
    try:
        return list(producto)[0]
    except:
        return {"error": "El producto no ha sido encontrado"}


#Retorna un usuario por id | PATH
@app.get("/usuario/{id}")
async def usuario(id: int):
    return buscar_usuario(id)


#Retorna un usuario por id | Query
@app.get("/usuarioquery/")
async def usuario(id: int):
    return buscar_usuario(id)

#Función buscar usuario
def buscar_usuario(id: int):
    usuario = filter(lambda usuario: usuario.id == id, Lista_usuarios)
    try:
        return list(usuario)[0]
    except:
        return {"error": "El usuario no fue encontrado"}

#Función crear usuario
@app.post("/usuario/")
async def usuario(nuevo_usuario: Usuario):
    if type(buscar_usuario(nuevo_usuario.id)) == Usuario:
        return {"error": "El usuario ya existe"}
    else:
        Lista_usuarios.append(nuevo_usuario)
        return nuevo_usuario

#Función crear producto
@app.post("/producto/")
async def producto(nuevo_producto: Producto):
    if type(buscar_producto(nuevo_producto.id)) == Producto:
        return {"error": "El producto ya existe"}
    else:
        Lista_productos.append(nuevo_producto)
        return nuevo_producto