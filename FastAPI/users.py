from fastapi import FastAPI

# Crear una instancia de FastAPI
app = FastAPI()

# Tenemos la url local, el servidor web local se ejecuta en el puerto 8000
# https://127.0.0.1:8000

# creamos el decorador @app.get("/users")
@app.get("/users")
# Creamos la funcion de operacion de ruta
async def users():
    """
    Operacion: GET
    Decorador: @app.get("/users")
    Funcion: async def users():
    devuelve un JSON con la lista de usuarios: ["users"]
    """
    return {"user1": "Manolo", "user2": "Juan", "user3": "Pedro"}

# Para iniciar el servidor con users usamos el siguiente comando:
# uvicorn users:app --reload



