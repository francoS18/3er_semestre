from TAD import Nodo_grafo, Arista

def grafo_recorrido(nodo_inicial, nodo_final):
    actual = nodo_inicial
    while True:
        siguiente=actual.conexiones[0].destino
        print(actual.valor,'->',siguiente.valor)
        if siguiente == nodo_final:
            break
        else:
            actual = actual.conexiones[0].destino
        

nodo_a = Nodo_grafo("A")
nodo_b = Nodo_grafo("B")
nodo_c = Nodo_grafo("C")
nodo_d = Nodo_grafo("D")
arista_ab = Arista(nodo_a, nodo_b)
arista_bc = Arista(nodo_b, nodo_c)
arista_cd = Arista(nodo_c, nodo_d)
arista_db = Arista(nodo_d, nodo_b)
nodo_a.agregar(arista_ab)
nodo_b.agregar(arista_bc)
nodo_c.agregar(arista_cd)
nodo_d.agregar(arista_db)

grafo_recorrido(nodo_a, nodo_d)
