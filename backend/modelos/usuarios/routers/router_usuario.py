from fastapi import APIRouter
from modelos.usuarios.models.model_usuario import Usuario

router = APIRouter()


#Variable usurio | db falsa
Lista_usuarios = [Usuario(id=1, nombre="Anaur", apellido="Martínez", edad=23),
                   Usuario(id=2, nombre="Ana", apellido="Lozano", edad=23),
                   Usuario(id=3, nombre="Carlos", apellido="Vegas", edad=30)]

#Retorna todos los usuarios
@router.get("/usuarios")
async def usuarios():
    return Lista_usuarios

#Retorna un usuario por id | PATH
@router.get("/usuario/{id}")
async def usuario(id: int):
    return buscar_usuario(id)


#Retorna un usuario por id | Query
@router.get("/usuarioquery/")
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
@router.post("/usuario/")
async def usuario(nuevo_usuario: Usuario):
    if type(buscar_usuario(nuevo_usuario.id)) == Usuario:
        return {"error": "El usuario ya existe"}
    else:
        Lista_usuarios.append(nuevo_usuario)
        return nuevo_usuario