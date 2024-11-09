from TAD import Nodo_grafo, Arista
nodo_a = Nodo_grafo("A")
nodo_b = Nodo_grafo("B")
nodo_c = Nodo_grafo("C")
arista_ab = Arista(nodo_a, nodo_b)
arista_bc = Arista(nodo_b, nodo_c)
arista_ca = Arista(nodo_c, nodo_a)
nodo_a.agregar(arista_ab)
nodo_b.agregar(arista_bc)
nodo_c.agregar(arista_ca)

print(nodo_a.conexiones[0].origen.valor, '->', nodo_a.conexiones[0].destino.valor)