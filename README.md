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

    Se desarrolla la seccion de Type Hints en el archivo 01_type_hints.py

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
    
