from TAD import ArbolBinarioBusqueda

def preorden(arbol):
    if arbol:
        print(arbol.cargaUtil)
        preorden(arbol.tieneHijoIzquierdo())
        preorden(arbol.tieneHijoDerecho())
        
def imprimirExpresion(arbol):
  valorCadena = ""
  if arbol:
      valorCadena = '(' + imprimirExpresion(arbol.tieneHijoIzquierdo())
      valorCadena = valorCadena + str(arbol.cargaUtil)
      valorCadena = valorCadena + imprimirExpresion(arbol.tieneHijoDerecho())+')'
  return valorCadena

miArbol = ArbolBinarioBusqueda()

miArbol.agregar(70, 'A') #Nodo Raíz
miArbol.agregar(23, 'D')
miArbol.agregar(73, 'F')
miArbol.agregar(93, 'E')
miArbol.agregar(31, 'B')
miArbol.agregar(14, 'C')
miArbol.agregar(94, 'G')
miArbol.agregar(105, 'H')
miArbol.agregar(92, 'I')

# Recorrido en Preorden
print(preorden(miArbol.raiz))

# Representación árbol binario con parentesis
print(imprimirExpresion(miArbol.raiz))
