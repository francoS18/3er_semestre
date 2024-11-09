from TAD import ListaEnlazadaCircular

def recorridoX(origen, n_ciclos):
    lista = ListaEnlazadaCircular()
    lista.agregar(5)
    lista.agregar(8)
    lista.agregar(11)
    lista.agregar(21)
    lista.agregar(28)
    lista.agregar(34)
    lista.agregar(41)
    contador = lista.count
    i = 1
    if contador > 0:
        xnodo = lista.head
        while i <= contador * n_ciclos:
            dato = xnodo.obtenerDato()
            if i == contador * n_ciclos:
                siguiente = lista.head.obtenerDato()
                xnodo = lista.head
            else:
                if xnodo.obtenerSiguiente().obtenerDato() == None:
                    siguiente = lista.head.obtenerDato()    
                else:
                    siguiente = xnodo.obtenerSiguiente().obtenerDato()
                xnodo = xnodo.obtenerSiguiente()
            print(dato, "->", siguiente)
            i = i + 1

recorridoX(11, 3)