class Contenedor:
    def __init__(self):
        self.cargas = ['USA', 'China', 'Japón', 'Australia', 'India', 'Alemania', 'Inglaterra', 'Chile']
        self.contador = 0

    def desapilar(self, pais):

        paisEliminado = []

        for i in self.cargas:
            if i == pais:
                self.contador = len(paisEliminado)
                self.cargas.append(paisEliminado[-1])
                return f'''La cantidad de datos cargas desapiladas es: {self.contador}'''
            elif i != pais:
                paisEliminado.append(i)
                self.cargas.pop(0)

class banco:
    def __init__(self):
        self.adultos = []

    def add_adulto(self, nombre, tipo_adulto):
        self.adultos.append([nombre, tipo_adulto])

    def get_adultos_mayores(self):
        adultos_mayores = []
        for adulto in self.adultos:
            if adulto[1] == 'AM':
                adultos_mayores.append(adulto[0])
        return adultos_mayores

    def get_adultos_jovenes(self):
        adultos_jovenes = []
        for adulto in self.adultos:
            if adulto[1] == 'AJ':
                adultos_jovenes.append(adulto[0])
        return adultos_jovenes

    def contar_adultos(self):
        contador_jovenes = 0
        contador_mayores = 0

        for adulto in self.adultos:
            if adulto[1] == 'AJ':
                contador_jovenes += 1
            elif adulto[1] == 'AM':
                contador_mayores += 1

        return contador_jovenes, contador_mayores
                
class ColaDoble:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def agregar_inicio(self, item):
        self.items.insert(0, item)

    def agregar_final(self, item):
        self.items.append(item)

    def eliminar_inicio(self):
        if not self.esta_vacia():
            return self.items.pop(0)

    def eliminar_final(self):
        if not self.esta_vacia():
            return self.items.pop()

    def obtener_inicio(self):
        if not self.esta_vacia():
            return self.items[0]

    def obtener_final(self):
        if not self.esta_vacia():
            return self.items[-1]

    def validar_documento_html(documento):
        cola_doble = ColaDoble()

        for caracter in documento:
            if caracter == '<':
                cola_doble.agregar_inicio(caracter)
            elif caracter == '>':
                if cola_doble.obtener_inicio() == '<':
                    cola_doble.eliminar_inicio()
                else:
                    return False

        return cola_doble.esta_vacia()