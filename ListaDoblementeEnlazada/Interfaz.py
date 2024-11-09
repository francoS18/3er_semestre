from TAD import ListaDoblementeEnlazada

def verLista(self):
        actual = self.cabeza
        while actual != None:
            print(actual.obtenerDato())
            actual = actual.obtenerSiguiente()
        
def valorAnterior(self, item):
    actual = self.cabeza
    encontrado = False
    while actual != None and not encontrado:
        if actual.obtenerDato() == item:
            encontrado = True
            return actual.obtenerAnterior().obtenerDato()
        else:
            actual = actual.obtenerSiguiente()
    return None

def valorSiguiente(self, item):
    actual = self.cabeza
    encontrado = False
    while actual != None and not encontrado:
        if actual.obtenerDato() == item:
            encontrado = True
            return actual.obtenerSiguiente().obtenerDato()
        else:
            actual = actual.obtenerSiguiente()
    return None