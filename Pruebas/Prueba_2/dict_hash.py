from TAD import TablaHash

def dict_append(clave, dato):
    tabla = TablaHash(30)
    index = tabla.funcionHash(clave)
    dictx = [None] * 30
    dictx[index] = dato
    return dictx

print(dict_append(15, 100000))
print(dict_append(18, 150000))
print(dict_append(128, 240000))
print(dict_append(56, 267000))
print(dict_append(333, 200000))
