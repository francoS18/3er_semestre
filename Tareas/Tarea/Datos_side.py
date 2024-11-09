import sys

# Tamaño de un entero
print('Enteros')
print(sys.getsizeof(0)) # 28
print(sys.getsizeof(1)) # 28

# Tamaño de un flotante
print('Flotantes')
print(sys.getsizeof(0.0)) # 24
print(sys.getsizeof(1.0)) # 24
print(sys.getsizeof(2.0**1000)) # 24

# Tamaño de un booleano
print('Booleanos')
print(sys.getsizeof(True)) # 28
print(sys.getsizeof(False)) # 28

# Tamaño de un string
print('Strings')
print(sys.getsizeof("")) # 49
print(sys.getsizeof("a")) # 50
print(sys.getsizeof("ab")) # 51
print(sys.getsizeof("abc")) # 52

# Tamaño de una lista
print('Listas')
print(sys.getsizeof([])) # 56
print(sys.getsizeof([0])) # 64
print(sys.getsizeof([0,1])) # 72

# Tamaño de un diccionario
print('Diccionarios')
print(sys.getsizeof({})) # 64
print(sys.getsizeof({"a":1})) # 184
print(sys.getsizeof({"a":1, "b":2})) # 184
print(sys.getsizeof({"a":1, "b":2, "c":3})) # 184

# Tamaño de un Set
print('Set')
print(sys.getsizeof(set())) # 216
print(sys.getsizeof({0})) # 216

# Tamaño de un objeto
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

print('Objetos')
print(sys.getsizeof(Persona("Juan"))) # 56

# Tamaño de frozenset
print('Frozenset')
print(sys.getsizeof(frozenset())) # 216
print(sys.getsizeof(frozenset({0}))) # 216

# Tamaño de un rango
print('Rangos')
print(sys.getsizeof(range(0))) # 48
print(sys.getsizeof(range(1))) # 48
# Tamaño de complex
print('Complejos')
print(sys.getsizeof(1+1j)) # 32

# Tamaño de una tupla
print('Tuplas')
print(sys.getsizeof(())) # 40
print(sys.getsizeof((0,))) # 48
print(sys.getsizeof((0,1))) # 56

# Tamaño de un byte
print('Bytes')
print(sys.getsizeof(b"")) # 33
print(sys.getsizeof(b"a")) # 34
print(sys.getsizeof(b"ab")) # 35
print(sys.getsizeof(b"abc")) # 36

# Tamaño de un bytearray
print('Bytearray')
print(sys.getsizeof(bytearray())) # 56
print(sys.getsizeof(bytearray(1))) # 57
print(sys.getsizeof(bytearray(2))) # 58
print(sys.getsizeof(bytearray(3))) # 59

# Tamaño de un memoryview
print('Memoryview')
print(sys.getsizeof(memoryview(bytearray()))) # 48
print(sys.getsizeof(memoryview(bytearray(1)))) # 49
print(sys.getsizeof(memoryview(bytearray(2)))) # 50

# Tamaño de NoneType
print('NoneType')
print(sys.getsizeof(None)) # 16

      
