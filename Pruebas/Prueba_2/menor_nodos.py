from TAD import ListaDoblementeEnlazada

def menor(origen, izquierda, derecha):
    lista = ListaDoblementeEnlazada()
    lista.agregar(5)
    lista.agregar(8)
    lista.agregar(11)
    lista.agregar(21)
    lista.agregar(28)
    lista.agregar(34)
    lista.agregar(41)
    nodo = lista.cabeza
    while nodo is not None:
        if nodo.dato == origen:
            if abs(izquierda - nodo.dato) == abs(derecha - nodo.dato):
                return izquierda,derecha
            elif abs(izquierda - nodo.dato) < abs(derecha - nodo.dato):
                return izquierda
            else:
                return derecha
        nodo = nodo.siguiente
    return None
