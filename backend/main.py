from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root ():
    return "Prueba"

@app.get("/listaproductos")
def listaproductos():
    return ["producto 1", "producto 2", "producto 3",]