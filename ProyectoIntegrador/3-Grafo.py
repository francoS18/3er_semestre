import heapq
from TAD import Arista,Nodo_grafo

class RedAerea:
    def __init__(self):
        self.ciudades = {}
    
    def agregar_ciudad(self, valor):
        nueva_ciudad = Nodo_grafo(valor)
        self.ciudades[valor] = nueva_ciudad
    
    def agregar_ruta(self, origen, destino, distancia):
        if origen not in self.ciudades:
            self.agregar_ciudad(origen)
        if destino not in self.ciudades:
            self.agregar_ciudad(destino)
        
        nueva_arista = Arista(origen, destino, distancia)
        self.ciudades[origen].agregar(nueva_arista)
        self.ciudades[destino].agregar(nueva_arista)  # No dirigido
    
    def encontrar_ruta_mas_corta(self, origen, destino):
        caminos_más_cortos = {valor: (None, float('infinity')) for valor in self.ciudades}
        caminos_más_cortos[origen] = (None, 0)
        pq = [(0, origen)]
        
        while pq:
            distancia_actual, ciudad_actual = heapq.heappop(pq)
            
            if distancia_actual > caminos_más_cortos[ciudad_actual][1]:
                continue
            
            for arista in self.ciudades[ciudad_actual].conexiones:
                ciudad_vecina = arista.destino
                distancia = distancia_actual + arista.distancia
                
                if distancia < caminos_más_cortos[ciudad_vecina][1]:
                    caminos_más_cortos[ciudad_vecina] = (ciudad_actual, distancia)
                    heapq.heappush(pq, (distancia, ciudad_vecina))
        
        # Reconstruir el camino más corto desde el destino hasta el origen
        camino = []
        nodo_actual = destino
        while nodo_actual is not None:
            camino.append(nodo_actual)
            nodo_actual = caminos_más_cortos[nodo_actual][0]
        camino.reverse()
        
        return camino

# Ejemplo de uso
red_aerea = RedAerea()

# Agregar ciudades y rutas
red_aerea.agregar_ruta("Ciudad A", "Ciudad B", 100)
red_aerea.agregar_ruta("Ciudad A", "Ciudad C", 200)
red_aerea.agregar_ruta("Ciudad B", "Ciudad D", 300)
red_aerea.agregar_ruta("Ciudad C", "Ciudad D", 150)

# Encontrar la ruta más corta entre dos ciudades
ruta_corta = red_aerea.encontrar_ruta_mas_corta("Ciudad A", "Ciudad D")
print("Ruta más corta:", ruta_corta)  # Output: ['Ciudad A', 'Ciudad C', 'Ciudad D'] 