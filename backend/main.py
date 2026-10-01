from fastapi import FastAPI

from modelos.usuarios.routers import router_usuario
from modelos.productos.routers import router_producto

app = FastAPI()

app.include_router(router_usuario.router)
app.include_router(router_producto.router)

@app.get("/")
async def root ():
    return "Prueba"

@app.get("/admin")
async def admin():
    return { "admin": "Anuar"}