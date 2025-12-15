# Crear una API con FastAPI en Python

# Importar FastAPI
from fastapi import FastAPI

# Crear una instancia de FastAPI
app = FastAPI()

# Crear una ruta de acceso GET, GET forma parte de las operaciones CRUD 
# (Create, Read, Update, Delete) disponibles en el protocolo HTTP
# CRUD con HTTP se refiere a como los metodos estandar HTTP 
# (GET, POST, PUT, PATCH, DELETE) se mapean a las operaciones fundamentales 
# de gestion de datos (Create, Read, Update, Delete) en APIs, permitiendo
# realizar operaciones CRUD a traves de peticiones HTTP.
@app.get("/") # / es localhost:8000, en nuestro caso https://127.0.0.1:8000

# Definir la funcion que se ejecutara cuando se acceda a la ruta GET
# En este caso, devolveremos un JSON con un mensaje

#async indica que la funcion es asincrona, sigue ejecutandose mientras 
# espera una respuesta
async def read_root(): 
    """Devuelve un JSON con un mensaje"""
    return {"Hello": "World"} # Clave:Valor

# Creamos otro metodo GET para practicar, devolveremos un JSON con una url
# En vez de en el directorio raiz (localhost:8000), lo ponemos en 
# /item (https://127.0.0.1:8000/item)
@app.get("/item")
async def read_item():
    """Devuelve un JSON con una url"""
    return {"Google": "https://www.google.com/"}

# Vemos que nos ha creado otro JSON con la url en la direccion especificada en el 
# GET