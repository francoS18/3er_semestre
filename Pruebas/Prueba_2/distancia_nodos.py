from TAD import ListaOrdenada

def distancia(origen, destino):
    lista = ListaOrdenada()
    lista.agregar(5)
    lista.agregar(8)
    lista.agregar(11)
    lista.agregar(21)
    lista.agregar(28)
    lista.agregar(34)
    lista.agregar(41)
    nodo = lista.cabeza
    contador = 0
    while nodo is not None:
        if nodo.dato == origen:
            while nodo.dato != destino:
                nodo = nodo.siguiente
                contador += 1
            break
        nodo = nodo.siguiente
    return contador
