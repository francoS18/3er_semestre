from TAD import ListaNoOrdenada

milista = ListaNoOrdenada()
milista.agregar(31)
milista.agregar(77)
milista.agregar(17)
milista.agregar(93)
milista.agregar(26)
milista.agregar(54)
print(milista.buscar(17))
print(milista.cabeza.obtenerDato())
print(milista.cabeza.obtenerSiguiente().obtenerDato())
print(milista.cabeza.obtenerSiguiente().obtenerSiguiente().obtenerDato())
print(milista.cabeza.obtenerSiguiente().obtenerSiguiente().obtenerSiguiente().obtenerDato())
print(milista.cabeza.obtenerSiguiente().obtenerSiguiente().obtenerSiguiente().obtenerSiguiente().obtenerDato())
print(milista.cabeza.obtenerSiguiente().obtenerSiguiente().obtenerSiguiente().obtenerSiguiente().obtenerSiguiente().obtenerDato())
# print(milista.cabeza.obtenerSiguiente().obtenerSiguiente().obtenerSiguiente().obtenerSiguiente().obtenerSiguiente().obtenerSiguiente())

# milista.agregar(42)
# milista.agregar(36)
# milista.agregar(55)
# milista.agregar(23)
# milista.agregar(65)
# milista.agregar(20)
# milista.agregar(17)
# milista.agregar(34)
# milista.agregar(11)

# def mostrar_lista(lista):

#     mi_lista = lista
#     while True:

#         try:
#             item = mi_lista.cabeza.obtener()
#             print(mi_lista.cabeza.obtener())
#             mi_lista.remove(item)
#         except:
#             break
    
# mostrar_lista(milista)
