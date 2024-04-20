# Implementación del TAD

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
    
    def primero(self):
        return self.items[0]
    
    def ultimo(self):
        return self.items[-1]
    
    def mostrar(self):
        return self.items
    
    