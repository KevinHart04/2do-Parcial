from typing import Any, Optional

from heap import HeapMin
from list_ import List
from queue_ import Queue
from stack import Stack

class Graph(List):

    class __nodeVertex:
        """Clase interna que representa un vértice en el grafo."""

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.edges = List()
            self.edges.add_criterion('value', Graph._order_by_value)
            self.edges.add_criterion('weight', Graph._order_by_weight)
            self.other_values = other_values
            self.visited = False
        
        def __str__(self):
            return self.value
    
    class __nodeEdge:
        """Clase interna que representa una arista en el grafo."""

        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            self.value = value
            self.weight = weight
            self.other_values = other_values # no esta en uso aun
        
        def __str__(self):
            return f'Destination: {self.value} with weight --> {self.weight}'
    
    def __init__(self, is_directed=False):
        """Inicializa un grafo, que puede ser dirigido o no dirigido."""
        self.add_criterion('value', self._order_by_value)
        self.is_directed = is_directed

    def _order_by_value(item):
        return item.value

    def _order_by_weight(item):
        return item.weight
    
    def show(
        self
    ) -> None:
        """Muestra la estructura del grafo, vértice por vértice con sus aristas."""
        for vertex in self:
            print(f"Vertex: {vertex}")
            vertex.edges.show() 

    def insert_vertex(
        self,
        value: Any,
        other_values: Optional[Any] = None
    ) -> None:
        """
        Inserta un nuevo vértice en el grafo.

        Args:
            value: El valor principal del vértice.
            other_values (optional): Un diccionario o objeto con datos adicionales.
        """
        node_vertex = Graph.__nodeVertex(value, other_values)
        self.append(node_vertex)

    def insert_edge(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None:
        """
        Inserta una arista entre dos vértices.
        Si el grafo es no dirigido, la arista se crea en ambas direcciones.
        """
        origin = self.search(origin_vertex, 'value')
        destination = self.search(destination_vertex, 'value')
        if origin is not None and destination is not None:
            node_edge = Graph.__nodeEdge(destination_vertex, weight)
            self[origin].edges.append(node_edge)
            if not self.is_directed and origin != destination:
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.append(node_edge)
        else:
            print('no se puede insertar falta uno de los vertices')

    def delete_edge(
        self,
        origin,
        destination,
        key_value: str = None,
    ) -> Optional[Any]:
        """
        Elimina una arista entre un origen y un destino.
        Si el grafo es no dirigido, intenta eliminar la arista en la dirección opuesta también.
        """
        pos_origin = self.search(origin, key_value)
        if pos_origin is not None:
            edge = self[pos_origin].edges.delete_value(destination, key_value)
            if self.is_directed and edge is not None:
                pos_destination = self.search(destination, key_value)
                if pos_destination is not None:
                    self[pos_destination].edges.delete_value(origin, key_value)
            return edge

    def delete_vertex(
        self,
        value,
        key_value_vertex: str = None,
        key_value_edges: str = 'value',
    ) -> Optional[Any]:
        """
        Elimina un vértice del grafo y todas las aristas que apuntan hacia él.
        """
        delete_value = g.delete_value(value, key_value_vertex)
        if delete_value is not None:
            for vertex in self:
                self.delete_edge(vertex.value, value, key_value_edges)
        return delete_value

    def mark_as_unvisited(self) -> None:
        """Marca todos los vértices del grafo como no visitados."""
        for vertex in self:
            vertex.visited = False

    def exist_path(self, origin, destination):
        """
        Verifica si existe un camino entre un vértice de origen y uno de destino.

        Returns:
            bool: True si existe un camino, False en caso contrario.
        """
        def __exist_path(graph, origin, destination):
            result = False
            vertex_pos = graph.search(origin, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    if graph[vertex_pos].value == destination:
                        return True
                    else:
                        for edge in graph[vertex_pos].edges:
                            destination_edge_pos = graph.search(edge.value, 'value')
                            if not graph[destination_edge_pos].visited:
                                result = __exist_path(graph, graph[destination_edge_pos].value, destination)
                                if result:
                                    break
            return result
        
        self.mark_as_unvisited()
        result = __exist_path(self, origin, destination)
        return result
    
    def deep_sweep(self, value) -> None:
        """Realiza un barrido en profundidad (DFS) del grafo desde un vértice de inicio."""
        def __deep_sweep(graph, value):
            vertex_pos = graph.search(value, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    print(graph[vertex_pos])
                    for edge in graph[vertex_pos].edges:
                        destination_edge_pos = graph.search(edge.value, 'value')
                        if not graph[destination_edge_pos].visited:
                            __deep_sweep(graph, graph[destination_edge_pos].value)

        self.mark_as_unvisited()
        __deep_sweep(self, value)
        
    def amplitude_sweep(self, value)-> None:
        """Realiza un barrido en amplitud (BFS) del grafo desde un vértice de inicio."""
        queue_vertex = Queue()
        self.mark_as_unvisited()
        vertex_pos = self.search(value, 'value')
        if vertex_pos is not None:
            if not self[vertex_pos].visited:
                self[vertex_pos].visited = True
                queue_vertex.arrive(self[vertex_pos])
                while queue_vertex.size() > 0:
                    vertex = queue_vertex.attention()
                    print(vertex.value)
                    for edge in vertex.edges:
                        destination_edge_pos = self.search(edge.value, 'value')
                        if destination_edge_pos is not None:
                            if not self[destination_edge_pos].visited:
                                self[destination_edge_pos].visited = True
                                queue_vertex.arrive(self[destination_edge_pos])

    def dijkstra(self, origin):
        """
        Calcula el camino más corto desde un vértice de origen a todos los demás vértices
        utilizando el algoritmo de Dijkstra.

        Args:
            origin: El valor del vértice de inicio.

        Returns:
            Stack: Una pila con la información del camino (destino, costo, predecesor).
        """
        from math import inf
        no_visited = HeapMin()
        path = Stack()

        # Inicializar todos los vértices con distancia infinita, excepto el origen (distancia 0)
        for vertex in self:
            distance = 0 if vertex.value == origin else inf
            no_visited.arrive([vertex.value, vertex, None], distance)
        
        while no_visited.size() > 0:
            # Seleccionar el nodo no visitado con la menor distancia
            value = no_visited.attention()
            costo_nodo_actual = value[0]
            path.push([value[1][0], costo_nodo_actual, value[1][2]])
            edges = value[1][1].edges
            for edge in edges:
                # Relajación de aristas: si se encuentra un camino más corto, se actualiza
                pos = no_visited.search(edge.value)
                if pos is not None:
                    if pos is not None:
                        if costo_nodo_actual + edge.weight < no_visited.elements[pos][0]:
                            no_visited.elements[pos][1][2] = value[1][0]
                            no_visited.change_priority(pos, costo_nodo_actual + edge.weight)
        return path

    def kruskal(self):
        """
        Encuentra el Árbol de Expansión Mínimo (MST) de un grafo no dirigido y ponderado
        utilizando el algoritmo de Kruskal.

        Returns:
            list: Una lista de tuplas, donde cada tupla representa una arista (origen, destino, peso) del MST.
        """
        def search_in_forest(forest, value):
            """Encuentra en qué sub-árbol (conjunto) del bosque se encuentra un valor."""
            for index, tree in enumerate(forest):
                if value in tree:
                    return index

        forest = [] # Lista de conjuntos (sub-árboles)
        edges = HeapMin() # Montículo de mínimos para todas las aristas
        mst = [] # Minimum Spanning Tree

        # Inicializar: cada vértice es un árbol en el bosque y todas las aristas se añaden al montículo
        for vertex in self:
            forest.append([vertex.value])
            for edge in vertex.edges:
                edges.arrive([vertex.value, edge.value], edge.weight)

        # Procesar aristas en orden de menor a mayor peso
        while len(forest) > 1 and edges.size() > 0:
            edge = edges.attention()
            origin_vertex, dest_vertex = edge[1]
            weight = edge[0]

            # Encontrar los árboles a los que pertenecen el origen y el destino de la arista
            origin = search_in_forest(forest, origin_vertex)
            destination = search_in_forest(forest, dest_vertex)

            if origin is not None and destination is not None:
                # Si no están en el mismo árbol (no forman un ciclo), unir los árboles y añadir la arista al MST
                if origin != destination:
                    forest[destination].extend(forest.pop(origin))
                    mst.append((origin_vertex, dest_vertex, weight))
        return mst


g = Graph(is_directed=True)

g.insert_vertex('T')
g.insert_vertex('F')
g.insert_vertex('R')
g.insert_vertex('X')
g.insert_vertex('Z')
# g.insert_vertex('A')
# g.insert_vertex('B')

g.insert_edge('T', 'X', 6)
g.insert_edge('T', 'F', 3)
g.insert_edge('T', 'R', 8)
g.insert_edge('F', 'X', 2)
g.insert_edge('F', 'R', 2)
g.insert_edge('R', 'X', 5)
g.insert_edge('Z', 'R', 4)
g.insert_edge('Z', 'X', 9)
# g.insert_edge('A', 'B', 15)

# g.show()
print(g.exist_path('T', 'Z'))
# expansion_tree = g.kruskal('F')
# print(expansion_tree)
# peso_total = 0
# for edge in expansion_tree.split(';'):
#     origin, destination, weight = edge.split('-')
#     print(f'origin {origin} destination {destination}')
#     peso_total += int(weight)
# print(f'peso total: {peso_total}')
# path = g.dijkstra('T')
# destination = 'Z'
# peso_total = None
# camino_completo = []

# while path.size() > 0:
#     value = path.pop()
#     if value[0] == destination:
#         if peso_total is None:
#             peso_total = value[1]
#         camino_completo.append(value[0])
#         destination = value[2]
# camino_completo.reverse()
# print(f'el camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}')

# vertex = g.delete_vertex('A', 'value')
# print(f'deleted vertex: {vertex}')

# g.amplitude_sweep('A')

# print()
# for vertex in g:
#     print(vertex.value, vertex.visited)
# g.show()
# print('segundo barrido')
# g.deep_sweep('I')

# es_adyacente(vértice, destino). Devuelve verdadero (true) si el destino es un nodo adyacente
# al vértice;
# adyacentes(vértice). Realiza un barrido de los nodos adyacentes al vértice;

# existe _paso(grafo, vértice origen, vértice destino). Devuelve verdadero (true) si es posible ir des-
# de el vértice origen hasta el vértice destino, caso contrario retornará falso (false);

# barrido_profundidad(grafo, vértice inicio). Realiza un barrido en profundidad del grafo a par-
# tir del vértice de inicio;

# barrido_amplitud(grafo, vértice inicio). Realiza un barrido en amplitud del grafo a partir del
# vértice de inicio;