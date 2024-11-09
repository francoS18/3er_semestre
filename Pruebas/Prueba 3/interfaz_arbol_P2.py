from TAD import ArbolBinarioBusqueda

arbol = ArbolBinarioBusqueda()

def postorden(arbol):
    if arbol:
        print(arbol.cargaUtil)
        postorden(arbol.tieneHijoIzquierdo())
        postorden(arbol.tieneHijoDerecho())

arbol.agregar(6, 'A') 
arbol.agregar(2, 'B')
arbol.agregar(8, 'C')
arbol.agregar(1, 'D')
arbol.agregar(4, 'E')
arbol.agregar(7, 'F')
arbol.agregar(9, 'G')
arbol.agregar(3, 'H')
arbol.agregar(5, 'I')

print(postorden(arbol.raiz))

