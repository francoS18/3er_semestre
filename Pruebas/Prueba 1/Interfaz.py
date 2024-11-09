from TAD import ListaNoOrdenada

milista = ListaNoOrdenada()

# Creando la lista
milista.agregar(66)
milista.agregar(23)
milista.agregar(31)
milista.agregar(19)
milista.agregar(56)
milista.agregar(20)
milista.agregar(45)
milista.agregar(34)
milista.agregar(52)

# agregando el elemento 38 al final de la lista
milista.anexar(38)

# agregando el elemento 49 en la posición 2 de la lista
milista.insertar(2,49)

# buscando la posicion del elemento 56
print(milista.indice(56))

#eliminadno el ultimo elemento y mostrandolo
print(milista.extraer())