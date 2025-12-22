from fastapi import FastAPI

# Importamos BaseModel de pydantic para crear un modelo de datos
from pydantic import BaseModel

# Crear una instancia de FastAPI
app = FastAPI()

# Tenemos la url local, el servidor web local se ejecuta en el puerto 8000
# https://127.0.0.1:8000

# creamos el decorador @app.get("/users")
@app.get("/users1")
# Creamos la funcion de operacion de ruta
async def users1():
    """
    Operacion: GET
    Decorador: @app.get("/users1")
    Funcion: async def users1():
    devuelve un JSON con la lista de usuarios: [{"user1"}, {"user2"}, {"user3"}]
    """
    return [{"nombre": "Manolo", "apellido": "Perez", "edad": 30}, 
    {"nombre": "Juan", "apellido": "Garcia", "edad": 25}, 
    {"nombre": "Pedro", "apellido": "Gonzalez", "edad": 40}]

# Para iniciar el servidor con users usamos el siguiente comando:
# uvicorn users:app --reload

# Vamos a crear un modelo de datos con BaseModel

# Creamos la entidad User que hereda de BaseModel
class User(BaseModel):
    """Entidad User que hereda de BaseModel
        param nombre: str
        param apellido: str
        param url: str
        param edad: int
    """
    nombre: str
    apellido: str
    url: str
    edad: int

# Basemodel permite crear un modelo de datos que se puede usar para validar los datos que se envian a la API
# parametros que se pueden usar con basemodel:

# # A continuacion creamos la operacion de ruta GET con el decorador @app.get("/users2")
@app.get("/users2")
async def users2():
    """
    Operacion: GET
    Decorador: @app.get("/users2")
    Funcion: async def users2():
    devuelve un JSON con el usuario: {"user1"}
    """

    # Con basemodel, validamos los datos que se envian a la API a traves de la entidad User
    return User(nombre= "Manolo", apellido= "Perez", url= "https://www.google.com/", edad= 30)

# Tenemos que pasarle varios usuarios, creamos una lista de usuarios con la entidad User
# Cada elemento de la lista es un objeto de la entidad User.
users = [User(nombre= "Manolo", apellido= "Perez", url= "https://www.google.com/", edad= 30),
User(nombre= "Juan", apellido= "Garcia", url= "https://www.google.com/", edad= 25),
User(nombre= "Pedro", apellido= "Gonzalez", url= "https://www.google.com/", edad= 40)]

@app.get("/users3")
async def users3():
    """
    Operacion: GET
    Decorador: @app.get("/users3")
    Funcion: async def users3():
    devuelve un JSON con la lista de usuarios: [{"user1"}, {"user2"}, {"user3"}]
    """
    return users


