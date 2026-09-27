from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root ():
    return "Prueba"

@app.get("/admin")
async def admin():
    return { "admin": "Anuar"}

@app.get("/listaproductos")
async def listaproductos():
    return {"productos": ["producto 1", "producto 2", "producto 3",]}