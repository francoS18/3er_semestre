from TAD import ListaOrdenada

Listaordenada = ListaOrdenada()
ListaOrdenada.extraer()
def obtenerLista(lista):
    listax = []
    nodox = lista.cabeza
    while True:
        try:
            listax.append(nodox.obtenerDato())
            nodox = nodox.obtenerSiguiente()
        except:
            break
    return listax    

def promedio(lista):
    valores_lista = obtenerLista(lista)
    sumar = 0
    tamaño_lista = len(valores_lista)

    for i in valores_lista:
        sumar += i 
    return sumar / tamaño_lista

def valorMinimo(lista):
    if lista.cabeza is None:
        return
    actual = lista.cabeza
    anterior = None
    while actual.obtenerSiguiente() is not None:
        anterior = actual
        actual = actual.obtenerSiguiente()
    if anterior is None:
        numero = lista.cabeza.obtenerDato()
    else:
        numero = actual.obtenerDato()
    return numero

def valorMaximo(lista):
    if lista.cabeza is None:
        return
    actual = lista.cabeza
    anterior = None
    while actual.obtenerSiguiente() is not None:
        anterior = actual
        actual = actual.obtenerSiguiente()
    if anterior is None:
        numero = lista.cabeza.obtenerDato()
    else:
        numero = actual.obtenerDato()
    return numero
    
def mediana(lista):
    valores_lista = obtenerLista(lista)

    if len(valores_lista) % 2 != 0:
        return valores_lista[len(valores_lista) // 2]
    else:
        return (valores_lista[len(valores_lista) // 2] + valores_lista[(len(valores_lista) // 2) - 1]) / 2

while True:
    anadir_numero = float(input('Ingrese un nuevo numero, si desea finalizar ingrese 0: '))
    if anadir_numero == 0:
        break
    else:
        Listaordenada.agregar(anadir_numero)

print(f'Valor minimo: {Listaordenada.cabeza.obtenerDato()}')
print(f'Valor maximo: {valorMaximo(Listaordenada)}')
print(f'Promedio: {promedio(Listaordenada)}')
print(f'Mediana: {mediana(Listaordenada)}')