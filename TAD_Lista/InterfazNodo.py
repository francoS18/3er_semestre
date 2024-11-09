from TAD import ListaNoOrdenada
milista = ListaNoOrdenada()

milista.agregar(31)
milista.agregar(77)
milista.agregar(17)
milista.agregar(93)
milista.agregar(26)
milista.agregar(54)

print(milista.cabeza.obtenerDato())
print(milista.cabeza.obtenerSiguiente().obtenerDato())
print(milista.cabeza.obtenerSiguiente().obtenerSiguiente().obtenerDato())
print(milista.cabeza.obtenerSiguiente().obtenerSiguiente().obtenerSiguiente().obtenerDato())