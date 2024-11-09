from TAD import Cola

cola = Cola()
print('''1) Ingresar un número a la cola 
2) Avanzar la cola y mostrar el número que sale 
3) Mostrar el contenido de la cola 
4) Salir ''')
while True:

    menu = int(input('Ingrese una opcion: '))
    if menu == 1:
        cola.agregar(int(input('Ingrese un numero ara agregarlo a la pila: ')))
    elif menu == 2:
        print(cola.avanzar())
    elif menu == 3:
        print(cola.items)
    elif menu == 4:
        break
