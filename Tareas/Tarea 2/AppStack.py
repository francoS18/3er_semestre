from TAD import Pila

pila = Pila()

print('''1) Agregar un número a la pila 
2) Quitar un número de la pila y mostrarlo 
3) Mostrar el contenido de la pila 
4) Salir''')
while True:
    menu = int(input('Ingrese una opcion: '))
    if menu == 1:
        pila.incluir(int(input('Ingrese un numero para agregarlo a la pila: ')))
    elif menu == 2:
        print(pila.extraer())
    elif menu == 3:
        print(pila.items)
    elif menu == 4:
        break
