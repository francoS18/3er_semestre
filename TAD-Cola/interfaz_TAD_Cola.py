# Interfaz del TAD

from TAD import Cola
from TAD import Cola2

# c=Cola()
# c.agregar('hola')
# c.agregar('perro')
# c.agregar(True)
# print(c.tamano())

# m =Cola2()

# # Agregando
# m.agregar('Pedro')
# m.agregar('Juan')
# m.agregar('Luisa')
# m.agregar('Diego')
# m.agregar('Alier')
# m.agregar('Boris')

# # Avamzar
# m.avanzar()

# # Primero
# print(m.primero())

# # Ultimo
# print(m.ultimo())

# # Tamano
# print(m.tamano())

# # Mostrar
# print(m.mostrar())

# RONDA
def ronda(saltos):
    for i in range(saltos):
        final = d.avanzar()
        d.agregar(final)
    return final
    
d = Cola()
d.agregar('Pedro')
d.agregar('Juan')
d.agregar('Claudia')
d.agregar('Diego')
d.agregar('Sofia')
d.agregar('Luisa')
d.agregar('Mario')

print(ronda(11))