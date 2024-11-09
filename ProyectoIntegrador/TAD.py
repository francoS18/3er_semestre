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
    

class ListaEnlazadaCircular:
    def __init__(self):
        self.head = None
        self.count = 0
     
    def agregar(self, data):
        self.insertar(data, self.count)
        return
     
    def insertar(self, data, index):
        if (index > self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
             
        if self.head == None:
            self.head = Nodo(data)
            self.count += 1
            return
         
        temp = self.head
        for _ in range(self.count - 1 if index - 1 == -1 else index - 1):
            temp = temp.siguiente
             
        aftertemp = temp.siguiente #New node goes between temp and aftertemp
        temp.siguiente = Nodo(data)
        temp.siguiente.siguiente = aftertemp
        if(index == 0):
            self.head = temp.siguiente
        self.count += 1
        return
     
    def remover(self, index):
        if (index >= self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
         
        if self.count == 1:
            self.head = None
            self.count = 0
            return
         
        before = self.head
        for _ in range(self.count - 1 if index - 1 == -1 else index - 1):
            before = before.siguiente
        after = before.siguiente.siguiente
         
        before.siguiente = after
        if(index == 0):
            self.head = after
        self.count -= 1
        return
     
    def indice(self, data):
        temp = self.head
        for i in range(self.count):
            if(temp.data == data):
                return i
            temp = temp.siguiente
        return None
     
    def tamano(self):
        return self.count
     
    def mostrar(self):
        print(self)


class Diccionario:
    def __init__(self):
        self.diccionario = {}

    def agregar(self, clave, valor):
        self.diccionario[clave] = valor

    def remover(self, clave):
        del(self.diccionario[clave])

    def verDato(self, clave):
        return self.diccionario[clave]



class TablaHash:
    def __init__(self, resumen):
        self.resumen = resumen
        self.tabla = [None] * resumen
    
    # Hash function
    def funcionHash(self, llave):
        hash = llave % self.resumen
        return hash

    def agregar(self, llave):
        hash = self.funcionHash(llave)
        if self.tabla[hash] is None:
            self.tabla[hash] = llave
   
    def buscar(self,llave):
        hash = self.funcionHash(llave);
        if self.tabla[hash] is None:
            return None
        else:
            return hash
  
    def remover(self,llave):
        hash = self.funcionHash(llave);
        if self.tabla[hash] is None:
            return False
        else:
            self.tabla[hash] is None;
            return True

class Nodo_grafo:
    def __init__(self, valor):
        self.valor = valor
        self.conexiones = []
    def agregar(self, arista):
        self.conexiones.append(arista)
        
class Arista:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino


class ArbolBinario:
    def __init__(self,objetoRaiz):
        self.clave = objetoRaiz
        self.hijoIzquierdo = None
        self.hijoDerecho = None

    def insertarIzquierdo(self,nuevoNodo):
        if self.hijoIzquierdo == None:
            self.hijoIzquierdo = ArbolBinario(nuevoNodo)
        else:
            t = ArbolBinario(nuevoNodo)
            t.hijoIzquierdo = self.hijoIzquierdo
            self.hijoIzquierdo = t

    def insertarDerecho(self,nuevoNodo):
        if self.hijoDerecho == None:
            self.hijoDerecho = ArbolBinario(nuevoNodo)
        else:
            t = ArbolBinario(nuevoNodo)
            t.hijoDerecho = self.hijoDerecho
            self.hijoDerecho = t

    def obtenerHijoDerecho(self):
        return self.hijoDerecho

    def obtenerHijoIzquierdo(self):
        return self.hijoIzquierdo

    def asignarValorRaiz(self,obj):
        self.clave = obj

    def obtenerValorRaiz(self):
        return self.clave

class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self


class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def agregar(self,clave,valor):
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = NodoArbol(clave,valor)
        self.tamano = self.tamano + 1

    def _agregar(self,clave,valor,nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                   self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                   nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                   self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                   nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)

    def __setitem__(self,c,v):
       self.agregar(c,v)

    def obtener(self,clave):
       if self.raiz:
           res = self._obtener(clave,self.raiz)
           if res:
                  return res.cargaUtil
           else:
                  return None
       else:
           return None

    def _obtener(self,clave,nodoActual):
       if not nodoActual:
           return None
       elif nodoActual.clave == clave:
           return nodoActual
       elif clave < nodoActual.clave:
           return self._obtener(clave,nodoActual.hijoIzquierdo)
       else:
           return self._obtener(clave,nodoActual.hijoDerecho)

    def __getitem__(self,clave):
       return self.obtener(clave)

    def __contains__(self,clave):
       if self._obtener(clave,self.raiz):
           return True
       else:
           return False

    def eliminar(self,clave):
      if self.tamano > 1:
         nodoAEliminar = self._obtener(clave,self.raiz)
         if nodoAEliminar:
             self.remover(nodoAEliminar)
             self.tamano = self.tamano-1
         else:
             raise KeyError('Error, la clave no está en el árbol')
      elif self.tamano == 1 and self.raiz.clave == clave:
         self.raiz = None
         self.tamano = self.tamano - 1
      else:
         raise KeyError('Error, la clave no está en el árbol')

    def __delitem__(self,clave):
       self.eliminar(clave)

    def empalmar(self):
       if self.esHoja():
           if self.esHijoIzquierdo():
                  self.padre.hijoIzquierdo = None
           else:
                  self.padre.hijoDerecho = None
       elif self.tieneAlgunHijo():
           if self.tieneHijoIzquierdo():
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoIzquierdo
                  else:
                     self.padre.hijoDerecho = self.hijoIzquierdo
                  self.hijoIzquierdo.padre = self.padre
           else:
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoDerecho
                  else:
                     self.padre.hijoDerecho = self.hijoDerecho
                  self.hijoDerecho.padre = self.padre

    def encontrarSucesor(self):
      suc = None
      if self.tieneHijoDerecho():
          suc = self.hijoDerecho.encontrarMin()
      else:
          if self.padre:
                 if self.esHijoIzquierdo():
                     suc = self.padre
                 else:
                     self.padre.hijoDerecho = None
                     suc = self.padre.encontrarSucesor()
                     self.padre.hijoDerecho = self
      return suc

    def encontrarMin(self):
      actual = self
      while actual.tieneHijoIzquierdo():
          actual = actual.hijoIzquierdo
      return actual

    def remover(self,nodoActual):
         if nodoActual.esHoja(): #hoja
           if nodoActual == nodoActual.padre.hijoIzquierdo:
               nodoActual.padre.hijoIzquierdo = None
           else:
               nodoActual.padre.hijoDerecho = None
         elif nodoActual.tieneAmbosHijos(): #interior
           suc = nodoActual.encontrarSucesor()
           suc.empalmar()
           nodoActual.clave = suc.clave
           nodoActual.cargaUtil = suc.cargaUtil

         else: # este nodo tiene un (1) hijo
           if nodoActual.tieneHijoIzquierdo():
             if nodoActual.esHijoIzquierdo():
                 nodoActual.hijoIzquierdo.padre = nodoActual.padre
                 nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
             elif nodoActual.esHijoDerecho():
                 nodoActual.hijoIzquierdo.padre = nodoActual.padre
                 nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
             else:
                 nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave,
                                    nodoActual.hijoIzquierdo.cargaUtil,
                                    nodoActual.hijoIzquierdo.hijoIzquierdo,
                                    nodoActual.hijoIzquierdo.hijoDerecho)
           else:
             if nodoActual.esHijoIzquierdo():
                 nodoActual.hijoDerecho.padre = nodoActual.padre
                 nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
             elif nodoActual.esHijoDerecho():
                 nodoActual.hijoDerecho.padre = nodoActual.padre
                 nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
             else:
                 nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave,
                                    nodoActual.hijoDerecho.cargaUtil,
                                    nodoActual.hijoDerecho.hijoIzquierdo,
                                    nodoActual.hijoDerecho.hijoDerecho)


