# Implementación del TAD

from datetime import date

class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):
         self.items.append(item)

     def extraer(self):
         return self.items.pop()

     def inspeccionar(self):
         return self.items[len(self.items)-1]

     def tamano(self):
         return len(self.items)


class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)

    def mostrar(self):
        return self.items
    
    def primero(self):
        return self.items[-1]
    
    def ultimo(self):
        return self.items[0]


class Cola2:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.append(item)

    def avanzar(self):
        return self.items.pop(0)

    def tamano(self):
        return len(self.items)

    def mostrar(self):
        return self.items
    
    def primero(self):
        return self.items[0]
    
    def ultimo(self):
        return self.items[-1]


class ColaDoble:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregarFrente(self, item):
        self.items.append(item)

    def agregarFinal(self, item):
        self.items.insert(0,item)

    def removerFrente(self):
        return self.items.pop()

    def removerFinal(self):
        return self.items.pop(0)

    def tamano(self):
        return len(self.items)

class Fecha:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def getDay(self):
        return self.day

    def getMonth(self):
        return self.month

    def getMonthName(self):
        if self.month==1:
            return "Enero"            
        if self.month==2:
            return "Febrero"            
        if self.month==3:
            return "Marzo"            
        if self.month==4:
            return "Abril"            
        if self.month==5:
            return "Mayo"            
        if self.month==6:
            return "Junio"            
        if self.month==7:
            return "Julio"            
        if self.month==8:
            return "Agosto"            
        if self.month==9:
            return "Septiembre"            
        if self.month==10:
            return "Octubre"            
        if self.month==11:
            return "Noviembre"            
        if self.month==12:
            return "Diciembre"            

    def getYear(self):
        return self.year
        
    def numDays(self, day2, month2, year2):
        fecha_pasada = date(year2, month2, day2)
        fecha_actual = date(self.year, self.month, self.day)
        return (fecha_actual - fecha_pasada).days

    def isLeapYear(self):
        if (self.year%4==0 and not self.year%100==0) or (self.year%100==0 and self.year%400==0):
            return True
        else:
            return False
    
    def compareTo(self,day2, month2, year2):
        fecha_pasada = date(year2, month2, day2)
        fecha_actual = date(self.year, self.month, self.day)
        if fecha_actual<fecha_pasada:
            return -1
        else:
            if fecha_actual>fecha_pasada:
                return 1
            else:
                return 0
    
    def str(self):
        fecha=date(self.year, self.month, self.day)
        string_fecha=fecha.strftime("%d/%m/%Y")
        return string_fecha
    
class Lista:

    def __init__(self):
        self.items = []

    def agregar(self, item):

        try:
            pos=self.items.index(item)
        except:
            self.items.insert(0,item)

    def remover(self, item):
        try:
            pos=self.items.index(item)
            self.items.pop(pos)
        except:
            pass

    def buscar(self, item):
        try:
            pos=self.items.index(item)
            return True
        except:
            return False

    def estaVacia(self):
        if len(self.items)==0:
            return True
        else:
            return False

    def tamano(self):
        return len(self.items)
    
    def anexar(self, item):
        try:
            pos=self.items.index(item)
        except:
            self.items.append(item)

    def indice(self, item):
        try:
            return self.items.index(item)
        except:
            pass
        
    def insertar(self, pos, item):
        try:
            pos=self.items.index(item)
        except:
            self.items.insert(pos,item)

    def extraer(self, *args):
        if len(args)==0:
            if len(self.items)>0:
                return (self.items.pop())
        else:
            if len(self.items)>0:
                pos=args[0]
                return(self.items.pop(pos))
            
class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente
    
        
class ListaNoOrdenada:

    def __init__(self):
        self.cabeza = None
        
    def estaVacia(self):
        return self.cabeza == None

    def agregar(self,item):
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp
    
    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()

        return contador
    
    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()

        return encontrado
    
    def remover(self,item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        if previo == None:
            self.cabeza = actual.obtenerSiguiente()
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())


class ListaOrdenada:
    def __init__(self):
        self.cabeza = None

    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        detenerse = False
        while actual != None and not encontrado and not detenerse:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                if actual.obtenerDato() > item:
                    detenerse = True
                else:
                    actual = actual.obtenerSiguiente()

        return encontrado

    def agregar(self,item):
        actual = self.cabeza
        previo = None
        detenerse = False
        while actual != None and not detenerse:
            if actual.obtenerDato() > item:
                detenerse = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        temp = Nodo(item)
        if previo == None:
            temp.asignarSiguiente(self.cabeza)
            self.cabeza = temp
        else:
            temp.asignarSiguiente(actual)
            previo.asignarSiguiente(temp)

    def estaVacia(self):
        return self.cabeza == None

    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()

        return contador
    
class ListaOrdenadaDescendente:
    def __init__(self):
        self.cabeza = None

    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        detenerse = False
        while actual != None and not encontrado and not detenerse:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                if actual.obtenerDato() > item:
                    detenerse = True
                else:
                    actual = actual.obtenerSiguiente()

        return encontrado

    def agregar(self,item):
        actual = self.cabeza
        previo = None
        detenerse = False
        while actual != None and not detenerse:
            if actual.obtenerDato() < item:
                detenerse = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        temp = Nodo(item)
        if previo == None:
            temp.asignarSiguiente(self.cabeza)
            self.cabeza = temp
        else:
            temp.asignarSiguiente(actual)
            previo.asignarSiguiente(temp)

    def estaVacia(self):
        return self.cabeza == None

    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()

        return contador

    def remover(self,item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        if previo == None:
            self.cabeza = actual.obtenerSiguiente()
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())


class Nodo2:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def obtenerAnterior(self):
        return self.anterior

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

    def asignarAnterior(self,nuevoanterior):
        self.anterior = nuevoanterior

class ListaDoblementeEnlazada:

    def __init__(self):
        self.cabeza = None
        
    def verLista(self):
        actual = self.cabeza
        while actual != None:
            print(actual.obtenerDato())
            actual = actual.obtenerSiguiente()
        
    def valorAnterior(self, item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
                return actual.obtenerAnterior().obtenerDato()
            else:
                actual = actual.obtenerSiguiente()
        return None
    
    def valorSiguiente(self, item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
                return actual.obtenerSiguiente().obtenerDato()
            else:
                actual = actual.obtenerSiguiente()
        return None
    
    def estaVacia(self):
        return self.cabeza == None

    def agregar(self,item):
        temp = Nodo2(item)
        temp.asignarSiguiente(self.cabeza)
        if self.cabeza is not None:
            self.cabeza.asignarAnterior(temp)
        self.cabeza = temp

  
    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()

        return contador