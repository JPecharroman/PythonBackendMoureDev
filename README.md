# PythonBackendMoureDev
## Curso Python para Backend siguiendo el curso de MoureDev

### 1. Que es un API?

    API (Application Programming Interface) es una forma de comunicación entre dos programas.

    Ref: https://es.wikipedia.org/wiki/API

    Capa de comunicación entre dos programas. En nuestro caso nos permitira comunicarnos con el backend o servidor.

### 2. Vamos a realizar este curso con el Framework [FastAPI](https://fastapi.tiangolo.com/), FastAPI es un framework para crear APIs con Python 3.7+ basado en [Starlette](https://www.starlette.io/) y [Pydantic](https://pydantic-docs.helpmanual.io/).

    ![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

    Ref: https://fastapi.tiangolo.com/

    Github: https://github.com/tiangolo/fastapi

    Para instalar FastAPI usamos el siguiente comando en la terminal (para abrir la terminal en antigravity crtl+shift+ñ):

    pip3 install fastapi

    a. FastAPI esta basado en estandares modernos de desarrollo de APIs, como el estandar HTTP/1.1 y el estandar JSON.

    b. FastAPI tambien usa el estandar [OpenAPI](https://github.com/OAI/OpenAPI-Specification), de la [iniciactiva OpenAPI](https://www.openapis.org/), (antes conocido como Swagger) para declaraciones de path operations, parametros, body request, seguridad,documentar las APIs, etc.

    c. Documentacion automatica del modelo de datos con [JSON Schema](https://json-schema.org/) (OpenAPI esta basado en JSON Schema).

    d. Generacion automatica de codigo de cliente para muchos lenguajes de programacion (como Python, JavaScript, TypeScript, etc.)

### 3. Que es JSON?

    JSON (JavaScript Object Notation) es un formato de intercambio de datos que se basa en una subconjunto del lenguaje de programación JavaScript.

    Sirve para almacenar e intercambiar datos entre un cliente y un servidor. Los datos se almacenan de un modo estructurado y entendible para los humanos.

    Ref: https://es.wikipedia.org/wiki/JSON

    Ejemplo de JSON:
    {
        "name": "Jorge",
        "age": 30,
        "city": "Madrid"
    }

    Los datos se almacenan en pares clave-valor. En este caso "name", "age" y "city" son las claves y "Jorge", 30 y "Madrid" son los valores.

    Es el estandar ideal para intercambiar datos entre sistemas, como un cliente y un servidor, por su simplicidad, eficiencia y compatibilidad con muchos lenguajes de programacion.

    Al final, sera la forma en que las APIs (Application Programming Interface) se comunican entre si.

### 4. Tipos en Python

    Python es un lenguaje de programacion dinamico, lo que significa que los tipos de datos se definen en tiempo de ejecucion.

    Python tiene soporte para los siguientes tipos de datos:

    a. Numericos: int, float, complex
    b. String: str
    c. Boolean: bool
    d. List: list
    e. Tuple: tuple
    f. Set: set
    g. Dictionary: dict

    Python tambien tiene soporte para los denominados "type hints", que son anotaciones que indican el tipo de datos que se espera que tenga una variable.

    Por ejemplo:

        nombre: str = "Jorge"
        edad: int = 30
        altura: float = 1.80
    
    En este caso, el tipo de datos de la variable "nombre" se espera que sea str, el tipo de datos de la variable "edad" se espera que sea int y el tipo de datos de la variable "altura" se espera que sea float.

    Declarando tipos de datos en Python es una buena practica, ya que permite al programador entender que tipo de datos se espera que tenga una variable.

    FastAPI usa type hints para validar los datos que se envian a la API.

    Se desarrolla la seccion de Type Hints en el archivo [01_type_hints.py](https://github.com/JPecharroman/PythonBackendMoureDev/blob/main/01_type_hints.py).

    FastAPI aprovecha los type hints para:
        a. Definir requisitos para los datos que se envian a la API, 
            desde request path parameters, query parameters, headers, 
            bodies, dependencies, etc.
        b. Convertir los datos que se envian a la API a los tipos de datos 
            que se esperan.
        c. Validar datos viniendo de cada request.
            Generacion de errores automaticos que se envian al cliente
            cuando los datos no cumplen con los requisitos definidos.
        e. Generar documentacion automatica de la API usando OpenAPI.
        f. Generar codigo de cliente para muchos lenguajes de programacion.
    
### 5. Instalacion de FastAPI

    Para instalar FastAPI usamos el siguiente comando en la terminal (para abrir la terminal en antigravity crtl+shift+ñ):

    pip3 install fastapi

    Al principio, para este tutorial, usaremos la version 0.124.4 de FastAPI y la
    instalaremos con todas sus dependencias:

    pip3 install fastapi[standard]

    Instalaremos tambien [uvicorn](https://www.uvicorn.dev/), que es un servidor web para ejecutar APIs en
    local, esto es, crearemos un servidor web local en nuestro ordenador para ejecutar nuestras APIs:

    pip3 install "uvicorn[standard]"

    **NOTA**: uvicorn es un servidor web para desarrollo, no es recomendado usarlo en producción.

    __a.__ Primeros Pasos con FastAPI

        Vamos a crear un archivo llamado `main.py` en la carpeta `FastAPI` y vamos a crear una API con FastAPI. 

    ```python 3.8+
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    ```

    Corremos la API con el siguiente comando:
    ```
    uvicorn main:app --reload
    ```
    Levantamos el servidor web local en nuestro ordenador para ejecutar nuestras APIs, main es el archivo principal y app es la instancia de FastAPI que creamos en el archivo main.py.

    --reload es un parametro que permite que el servidor se recargue automaticamente cuando detecte cambios en el codigo.

    Para detener el servidor web local, usamos el siguiente comando:
    ```
    Ctrl + C
    ```

    Nos devolvera un JSON con el siguiente contenido:
    ```json
    {
        "Hello": "World"
    }
    ```
    Como vemos este JSON?, entramos en la direccion que nos indica el servidor web local, que es http://127.0.0.1:8000/.

    Si entramos en esta direccion, veremos la misma informacion que nos devuelve la API.

    Si entramos en la direccion http://127.0.0.1:8000/docs/ veremos la documentacion de la API, realizada por [Swagger](https://swagger.io/).

    Si entramos en la direccion http://127.0.0.1:8000/redoc/ veremos la documentacion de la API, realizada por [ReDoc](https://redocly.com/).


    Dentro del archivo main.py se define una ruta de acceso GET, que es la ruta de acceso por defecto de la API.

    GET forma parte de las operaciones CRUD (Create, Read, Update, Delete) disponibles en el protocolo HTTP.
    CRUD con HTTP se refiere a como los metodos estandar HTTP (GET, POST, PUT, PATCH, DELETE) se mapean a las operaciones fundamentales de gestion de datos (Create, Read, Update, Delete) en APIs, permitiendo realizar operaciones CRUD a traves de peticiones HTTP.

    Mapeo de operaciones CRUD con HTTP:
    - Crear(Create): usamos la operacion POST
    - Leer(Read): usamos la operacion GET
    - Actualizar(Update): usamos la operacion PUT
    - Eliminar(Delete): usamos la operacion DELETE

    GET es la operacion por defecto de la API, es decir, cuando accedemos a la ruta de acceso GET, se ejecuta la operacion GET por defecto.

    Aplicaciones externas para poder realizar peticiones HTTP:

    - [Postman](https://www.postman.com/)

        La mas usada y la mas completa.
        "Unifique el diseño, las pruebas, la documentación, la supervisión y el descubrimiento de API en una plataforma que se integra con el resto de su pila, incluidas todas las principales puertas de enlace y soluciones Git."

    - [Insomnia](https://insomnia.rest/)

        "Una plataforma de colaboración API nativa de IA para desarrolladores que no paran de desarrollar. Prueba, depura y diseña cualquier punto final con soporte para clientes MCP, capacidades basadas en IA y flujos de trabajo fluidos locales, en Git o en la nube."

    - [cURL](https://curl.se/)

        "Herramienta de línea de comandos y biblioteca para transferir 
        datos con URL."

    - [HTTPie](https://httpie.io/)

        "HTTPie está haciendo que las API sean simples e intuitivas para 
        quienes construyen las herramientas de nuestro tiempo."


    Extensiones para Visual Studio Code, o Antigravity, para instalar extensiones en VSCode usar ctrl+shift+x:

    - Thunder Client: Thunder Client es una extensión de cliente API Rest ligera para VS Code. (Al tiempo de escribir este README, no se puede usar en Antigravity gratuitamente, la usaremos desde VSCode)

    - REST Client: REST Client es una extensión de cliente API Rest que permite enviar solicitudes HTTP y ver la respuesta en Visual Studio Code directamente.

    - 

### 6. Crear una operacion de la ruta

    Path, ruta, ultima parte de la URL, a partir de la primera barra (/).

    En la direccion https://127.0.0.1:8000/item el path es /item, en una direccion como https://127.0.0.1:8000/item/1 el path es /item/1

    Operaciones CRUD con HTTP, aqui nos referimos a uno de los metodos HTTP que usamos para realizar operaciones CRUD (Create, Read, Update, Delete):
    - Crear(Create): usamos la operacion POST
    - Leer(Read): usamos la operacion GET
    - Actualizar(Update): usamos la operacion PUT
    - Eliminar(Delete): usamos la operacion DELETE

    Tenemos otras cuatro opciones menos usuales:
    - PATCH: sirve para actualizar una parte de un recurso, usamos la operacion PATCH
    - OPTIONS: sirve para obtener informacion sobre los metodos HTTP que se pueden usar con un recurso, usamos la operacion OPTIONS
    - HEAD: sirve para obtener informacion sobre un recurso, usamos la operacion HEAD
    - TRACE: sirve para depurar una peticion HTTP, usamos la operacion TRACE

    En el protocolo HTTP, te puedes comunicar con cada path usando uno, o varios, de estos metodos HTTP.

    En main.py, linea 15, vemos la operacion GET, y el path "/" en el comando @app.get("/").
    Este comando indica a FastAPI que la operacion GET se va a ejecutar cuando se acceda al path "/".

    ** @decorator **
    A @algo en python se le llama decorator, decorador, esto es porque va encima de una funcion, como si fuera un sombrero.
    Un decorador coge la funcion que esta inmediatamente debajo y hace algo con ella.
    En este caso, el decorador @app.get("/") le dice a FastAPI que la funcion a continuacion corresponde a la operacion GET del path "/".
    Este es el "decorador de operacion de trayectoria".

    Otros decoradores:
    - @app.post("/")
    - @app.put("/")
    - @app.delete("/")

    - @app.patch("/")
    - @app.options("/")
    - @app.head("/")
    - @app.trace("/")
    
### 7. Crear una funcion para la operacion de ruta

    Volvamos a main.py, tenemos:

    """
    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    """
    
    Donde:
    - Ruta o path: /
    - Operacion: GET
    - Decorador: @app.get("/")
    - Funcion: async def root():
        - async: indica que la funcion es asincrona, sigue ejecutandose mientras espera una respuesta
        - root: nombre de la funcion

    Esta funcion sera llamada por FastAPI cuando se acceda al path "/" con la operacion GET.

    Para devolver el contenido de la funcion, usamos el comando return. Podemos devolver un diccionario, una lista, un string, un numero, etc.
    """
    return {"message": "Hello World"}
    """

### 8. Uso de modelado de datos con BaseModel para FastAPI

    Lo primero que necesitamos es importar la clase BaseModel de la libreria pydantic.
    
    """
    from pydantic import BaseModel
    """

    Luego creamos una clase que hereda de BaseModel, y le indicamos los campos que queremos que tenga.
    """
    class User(BaseModel):
        nombre: str
        apellido: str
        url: str
        edad: int
    """

    BaseModel permite crear un modelo de datos que se puede usar para validar los datos que se envian a la API a traves de la entidad User, esto es, no tenemos que crear un modelo de datos para cada operacion de ruta.

    A continuacion crearemos una lista con los usuarios que tengamos usando la entidad User.

    """
    lista_usuarios = [User(nombre= "Manolo", apellido= "Perez", url= "https://www.google.com/", edad= 30),
    User(nombre= "Juan", apellido= "Garcia", url= "https://www.google.com/", edad= 25),
    User(nombre= "Pedro", apellido= "Gonzalez", url= "https://www.google.com/", edad= 40)]
    """

    Ya tenemos nuestros usuarios en una lista preparada para pasarla a la API.

    """
    @app.get("/users")
    async def users():
        return lista_usuarios
    """

    Hemos pasado nuestra lista de usuarios al servidor web a través de la API, ahora podemos acceder a ella desde el navegador.
    


