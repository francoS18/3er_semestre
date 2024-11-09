from TAD import ArbolBinarioBusqueda

arbol = ArbolBinarioBusqueda()

def preorden(arbol):
    if arbol:
        preorden(arbol.tieneHijoIzquierdo())
        preorden(arbol.tieneHijoDerecho())

def imprimirExpresion(arbol):
    valorCadena = ""
    if arbol:
        valorCadena = '(' + imprimirExpresion(arbol.tieneHijoIzquierdo())
        valorCadena = valorCadena + str(arbol.cargaUtil)
        valorCadena = valorCadena + imprimirExpresion(arbol.tieneHijoDerecho())+')'
    return valorCadena

arbol.agregar(6, 'A') 
arbol.agregar(2, 'B')
arbol.agregar(8, 'C')
arbol.agregar(1, 'D')
arbol.agregar(4, 'E')
arbol.agregar(7, 'F')
arbol.agregar(9, 'G')
arbol.agregar(3, 'H')
arbol.agregar(5, 'I')

print(imprimirExpresion(arbol.raiz))
