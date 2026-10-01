from fastapi import APIRouter
from modelos.productos.models.model_producto import Producto


router = APIRouter()

#Variable producto | db falsa
Lista_productos = [Producto(id=1, nombreP="Pizza", precio="60000"), 
                    Producto(id=2, nombreP="Hamburguesa", precio="50000"),
                    Producto(id=3, nombreP="Pasta", precio="45000")]

#Retorna todos los productos
@router.get("/productos")
async def productos():
    return Lista_productos


#Retorna un producto por id | PATH
@router.get("/producto/{id}")
async def producto(id: int):
    return buscar_producto(id)


#Retorna un producto por id | Query
@router.get("/productoquery/")
async def producto(id: int):
    return buscar_producto(id)

#Función buscar producto
def buscar_producto(id: int):
    producto = filter(lambda producto: producto.id == id, Lista_productos)
    try:
        return list(producto)[0]
    except:
        return {"error": "El producto no ha sido encontrado"}

#Función crear producto
@router.post("/producto/")
async def producto(nuevo_producto: Producto):
    if type(buscar_producto(nuevo_producto.id)) == Producto:
        return {"error": "El producto ya existe"}
    else:
        Lista_productos.append(nuevo_producto)
        return nuevo_producto