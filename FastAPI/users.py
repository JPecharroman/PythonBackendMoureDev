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


# Vamos a ver ahora como usar el path para pasar parametros a la API, para ellos tendremos que redefinir nuestro modelo de datos
class lista_usuarios(BaseModel):
    """Entidad lista_usuarios que hereda de BaseModel
        param clave: int
        param nombre: str
        param apellido: str
        param url: str
        param edad: int
    """
    clave: int
    nombre: str
    apellido: str
    url: str
    edad: int

# Creamos una lista de usuarios con la entidad lista_usuarios
usuarios = [lista_usuarios(clave= 1, nombre= "Manolo", apellido= "Perez", url= "https://www.google.com/", edad= 30),
lista_usuarios(clave= 2, nombre= "Juan", apellido= "Garcia", url= "https://www.google.com/", edad= 25),
lista_usuarios(clave= 3, nombre= "Pedro", apellido= "Gonzalez", url= "https://www.google.com/", edad= 40)]

#Usamos el path para pasarle el parametro clave a la API, en este caso usamos el campo clave para pedir el usuario que necesitamos.
@app.get("/users4/{clave}")
async def users4(clave: int):
    """
    Operacion: GET
    Decorador: @app.get("/users/{clave}")
    Funcion: async def users4(clave: int):
    devuelve un JSON con el usuario: {"user1"}
    """
    return usuarios[clave]

# Para poder pasarle el parametro user_id a la API, debemos usar el path, por ejemplo:
# https://127.0.0.1:8000/users4/1, recordar que la clave empieza en 0, el primer usuario tiene la clave 0, el segundo usuario tiene la clave 1, etc.

# Bien, ahora yo quiero que el parametro pasado en el path se corresponda con el valor del campo pasado como clave, por ejemplo, si el dni es 27, si yo le paso el 
# valor 27 al path, me devolvera el usuario con dni 27.

class usuario(BaseModel):
    """Entidad usuario que hereda de BaseModel
        param dni: int
        param nombre: str
        param apellido: str
        param edad: int
    """
    dni: int
    nombre: str
    apellido: str
    edad: int

# Creamos una lista de usuarios con la entidad usuario
usuarios = [usuario(dni= 34567890, nombre= "Manolo", apellido= "Perez", edad= 30),
usuario(dni= 23456789, nombre= "Juan", apellido= "Garcia", edad= 25),
usuario(dni= 12345678, nombre= "Pedro", apellido= "Gonzalez", edad= 40)]

# Vamos a pasarle como parametro a la funcion el dni de la persona que queremos buscar. En el Path buscaremos el dni de la persona que queremos buscar, 
# en este caso la primera

@app.get("/users5/{dni}")
async def users5(dni: int):
    """
    Funcion: async def users5(dni: int):
    devuelve un JSON con el usuario: {"user1"}
    """
    usuarios_filtrados = filter(lambda x: x.dni == dni, usuarios)
    # Con filter, funcion de orden superior, realizamos una busqueda en la lista de usuarios mediante una lambda
    # que compara el dni de cada usuario con el dni que le pasamos como parametro.
    # Filter devuelve un objeto, asi que tenemos que guardar el resultado en una variable.
    
    # Con list, convertimos el objeto devuelto por filter en una lista.
    # Con [0], obtenemos el primer elemento de la lista.
    
    return list(usuarios_filtrados)[0]

# Para poder pasarle el parametro dni a la API, debemos usar el path, por ejemplo:
# https://127.0.0.1:8000/users5/34567890, recordar que el dni empieza en 0, el primer usuario tiene el dni 0, el segundo usuario tiene el dni 1, etc.

