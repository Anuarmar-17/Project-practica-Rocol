from fastapi import APIRouter
from typing import Optional
from modules.products.models.model_product import Product


router = APIRouter(
    prefix="/product",
    tags=["Products"]
)

#Variable producto | db falsa
product_list = [Product(id=1, nameP="Pizza", price="60000"), 
                    Product(id=2, nameP="Hamburguesa", price="50000"),
                    Product(id=3, nameP="Pasta", price="45000")]

#Retorna todos los productos y por id | Query
@router.get("/")
async def products(id: Optional[int] = None):
    if id is not None:
        return search_product(id)

    return product_list

#Retorna un producto por id | PATH
@router.get("/{id}")
async def product(id: int):
    return search_product(id)

#Función crear producto
@router.post("/")
async def product(new_product: Product):
    if type(search_product(new_product.id)) == Product:
        return {"error": "El producto ya existe"}
    else:
        product_list.append(new_product)
        return new_product

#Función buscar producto
def search_product(id: int):
    product = filter(lambda product: product.id == id, product_list)
    try:
        return list(product)[0]
    except:
        return {"error": "El producto no ha sido encontrado"}