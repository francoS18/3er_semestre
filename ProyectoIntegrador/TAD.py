# Tabla Hash
class TablaHash:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tabla = [None] * tamano

    def funcionHash(self, clave):
        return clave % self.tamano

    def agregar(self, clave, valor):
        direccion = self.funcionHash(clave)
        if self.tabla[direccion] is None:
            self.tabla[direccion] = [(clave, valor)]
        else:
            self.tabla[direccion].append((clave, valor))

    def obtener(self, clave):
        direccion = self.funcionHash(clave)
        if self.tabla[direccion] is None:
            return None
        else:
            for par in self.tabla[direccion]:
                if par[0] == clave:
                    return par[1]
            return None

    def eliminar(self, clave):
        direccion = self.funcionHash(clave)
        if self.tabla[direccion] is None:
            return None
        else:
            for i in range(len(self.tabla[direccion])):
                if self.tabla[direccion][i][0] == clave:
                    self.tabla[direccion].pop(i)
                    return True
            return False

    def mostrar(self):
        for i in range(self.tamano):
            if self.tabla[i] is not None:
                print(str(i) + " " + str(self.tabla[i]))
            else:
                print(str(i) + " " + str(self.tabla[i]))

# Diccionario de Datos
class DiccionarioDatos:
    def __init__(self):
        self.tabla = TablaHash(100)

    def agregar(self, clave, valor):
        self.tabla.agregar(clave, valor)

    def obtener(self, clave):
        return self.tabla.obtener(clave)

    def eliminar(self, clave):
        return self.tabla.eliminar(clave)

    def mostrar(self):
        self.tabla.mostrar()

# Grafos
class Grafo:
    def __init__(self):
        self.vertices = []
        self.matriz = []

    def agregarVertice(self, vertice):
        self.vertices.append(vertice)
        for fila in self.matriz:
            fila.append(0)
        self.matriz.append([0] * len(self.vertices))

    def agregarArista(self, vertice1, vertice2):
        indice1 = self.vertices.index(vertice1)
        indice2 = self.vertices.index(vertice2)
        self.matriz[indice1][indice2] = 1
        self.matriz[indice2][indice1] = 1

    def mostrar(self):
        for i in range(len(self.vertices)):
            print(self.vertices[i], end=": ")
            for j in range(len(self.vertices)):
                if self.matriz[i][j] == 1:
                    print(self.vertices[j], end=" ")
            print()

# NodoB
class NodoB:
    def __init__(self, grado, es_hoja):
        self.grado = grado
        self.es_hoja = es_hoja
        self.valores = [None] * (2 * grado - 1)
        self.hijos = [None] * (2 * grado)

    def insertar_no_lleno(self, valor):
        i = self.n - 1
        if self.es_hoja:
            while i >= 0 and self.valores[i] > valor:
                self.valores[i + 1] = self.valores[i]
                i -= 1
            self.valores[i + 1] = valor
            self.n += 1
        else:
            while i >= 0 and self.valores[i] > valor:
                i -= 1
            if self.hijos[i + 1].n == 2 * self.grado - 1:
                self.dividir(i + 1, self.hijos[i + 1])
                if self.valores[i + 1] < valor:
                    i += 1
            self.hijos[i + 1].insertar_no_lleno(valor)

    def dividir(self, i, nodo):
        nuevo_nodo = NodoB(nodo.grado, nodo.es_hoja)
        nuevo_nodo.n = self.grado - 1
        for j in range(self.grado - 1):
            nuevo_nodo.valores[j] = nodo.valores[j + self.grado]
        if not nodo.es_hoja:
            for j in range(self.grado):
                nuevo_nodo.hijos[j] = nodo.hijos[j + self.grado]
        nodo.n = self.grado - 1
        for j in range(self.n, i, -1):
            self.hijos[j + 1] = self.hijos[j]
        self.hijos[i + 1] = nuevo_nodo
        for j in range(self.n - 1, i - 1, -1):
            self.valores[j + 1] = self.valores[j]
        self.valores[i] = nodo.valores[self.grado - 1]
        self.n += 1

    def mostrar(self):
        for i in range(self.n):
            if self.es_hoja is False:
                self.h

# Arbol-B
class ArbolB:
    def __init__(self, grado):
        self.grado = grado
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = NodoB(self.grado, True)
            self.raiz.valores[0] = valor
            self.raiz.n = 1
        else:
            if self.raiz.n == 2 * self.grado - 1:
                nueva_raiz = NodoB(self.grado, False)
                nueva_raiz.hijos[0] = self.raiz
                nueva_raz.dividir(0, self.raiz)
                i = 0
                if nueva_raiz.valores[0] < valor:
                    i += 1
                nueva_raiz.hijos[i].insertar_no_lleno(valor)
                self.raiz = nueva_raiz
            else:
                self.raiz.insertar_no_lleno(valor)

    def mostrar(self):
        if self.raiz is not None:
            self.raiz.mostrar()

