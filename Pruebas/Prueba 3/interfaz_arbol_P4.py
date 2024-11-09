from TAD import ArbolBinarioBusqueda
from interfaz_arbol_P1 import imprimirExpresion

arbol = ArbolBinarioBusqueda()

def nodosHoja(arbol):
    nodos = []
    expresion = imprimirExpresion(arbol)
    for i in range(len(expresion)):
        if expresion[i] == '(' and expresion[i+2] == ')':
            nodos.append(expresion[i+1])
    return nodos

arbol.agregar(6, 'A') 
arbol.agregar(2, 'B')
arbol.agregar(8, 'C')
arbol.agregar(1, 'D')
arbol.agregar(4, 'E')
arbol.agregar(7, 'F')
arbol.agregar(9, 'G')
arbol.agregar(3, 'H')
arbol.agregar(5, 'I')

print(nodosHoja(arbol.raiz))