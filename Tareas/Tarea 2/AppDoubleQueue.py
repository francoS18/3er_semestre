from TAD import ColaDoble

cola_doble = ColaDoble()
print('''########## MENU ##########
1) Ingresar un número al frente de la cola 
2) Ingresar un número al final de la cola 
3) Avanzar el frente de la cola y mostrar el número que sale 
4) Avanzar al final de la cola y mostrar el número que sale 
5) Mostrar el contenido de la cola 
6) Salir''')
while True:

    menu = int(input('Ingrese una opcion: '))
    if menu == 1:
        cola_doble.agregarFrente(int(input('Ingrese un numero ara agregarlo a la pila: ')))
    elif menu == 2:
        cola_doble.agregarFinal(int(input('Ingrese un numero ara agregarlo a la pila: ')))
    elif menu == 3:
        print(cola_doble.removerFrente())
    elif menu == 4:
        print(cola_doble.removerFinal())
    elif menu == 5:
        print(cola_doble.items)    
    elif menu == 6:
        break
