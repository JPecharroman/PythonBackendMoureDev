# Type Hints en Python

# Tipos de datos con su Type Hint

# Numericos
numero: int = 1
numero_decimal: float = 1.1
numero_complejo: complex = 1 + 1j

# Texto
texto: str = "Hola"
texto2: str = 'Hola'
texto3: str = '''Hola'''
texto4: str = """Hola"""

# Booleano
booleano: bool = True
booleano2: bool = False

# Lista
lista: list = [1, 2, 3]
tupla: tuple = (1, 2, 3)
conjunto: set = {1, 2, 3}
diccionario: dict = {"a": 1, "b": 2, "c": 3}

# Otros
nulo: None = None

# Forma de determinar cual es el tipo de dato de una variable con la funcion type()
print(type(numero))
print(type(texto))
print(type(booleano))
print(type(lista))
print(type(conjunto))
print(type(diccionario))
print(type(nulo))

# Darle un type hint a una variable da informacion al programa sobre que metodos 
# se, espera, pueden usar con esa variable. Si es de tipo entero podran usarse 
# metodos asociados a numeros enteros, raiz cuadrada, etc.
# si es de tipo texto podran usarse metodos asociados a cadenas de texto, convertir
# mayusculas, minusculas, etc.



