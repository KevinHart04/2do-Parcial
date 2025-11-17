from graph import Graph
from console_colors import Colors

# --- Datos del Grafo ---

characters_data = [
    {"name": "Luke Skywalker", "episodes": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    {"name": "Darth Vader", "episodes": [3, 4, 5, 6]},
    {"name": "Yoda", "episodes": [1, 2, 3, 5, 6, 8]},
    {"name": "Boba Fett", "episodes": [2, 4, 5, 6]},
    {"name": "C-3PO", "episodes": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    {"name": "Leia", "episodes": [3, 4, 5, 6, 7, 8, 9]},
    {"name": "Rey", "episodes": [7, 8, 9]},
    {"name": "Kylo Ren", "episodes": [7, 8, 9]},
    {"name": "Chewbacca", "episodes": [3, 4, 5, 6, 7, 8, 9]},
    {"name": "Han Solo", "episodes": [4, 5, 6, 7]},
    {"name": "R2-D2", "episodes": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    {"name": "BB-8", "episodes": [7, 8, 9]},
    {"name": "Darth Maul", "episodes": [1]},
    {"name": "Obi-Wan Kenobi", "episodes": [1, 2, 3, 4, 5, 6]},
]

edges_data = [
    ("Luke Skywalker", "Darth Vader", 4),
    ("Luke Skywalker", "Leia", 5),
    ("Luke Skywalker", "Han Solo", 4),
    ("Luke Skywalker", "Yoda", 3),
    ("Luke Skywalker", "R2-D2", 7),
    ("Darth Vader", "Obi-Wan Kenobi", 2),
    ("Yoda", "Obi-Wan Kenobi", 3),
    ("Yoda", "Boba Fett", 1),
    ("C-3PO", "R2-D2", 9),
    ("C-3PO", "Leia", 6),
    ("Leia", "Han Solo", 4),
    ("Rey", "Kylo Ren", 3),
    ("Rey", "BB-8", 3),
    ("Han Solo", "Chewbacca", 4),
]

# --- Creación y Población del Grafo ---

sw_graph = Graph(is_directed=False)

print(f"{Colors.BOLD_GREEN}Cargando personajes en el grafo...{Colors.RESET}")
for char in characters_data:
    sw_graph.insert_vertex(char["name"], other_values={"episodes": char["episodes"]})

for origin, dest, weight in edges_data:
    sw_graph.insert_edge(origin, dest, weight)

print(f"{Colors.BOLD_GREEN}Grafo de Star Wars creado.{Colors.RESET}")

# --- Resolución de los puntos del ejercicio ---

# b. Hallar el árbol de expansión mínimo que conecta a los personajes.
#    El algoritmo de Kruskal encuentra el MST para todo el grafo (o para cada componente conexa).
#    Esto asegura que todos los personajes, incluyendo C-3PO, Yoda y Leia, estén conectados
#    de la forma más "barata" posible si pertenecen a la misma componente.
print(f"\n--- {Colors.BOLD_BLUE}b. Árbol de Expansión Mínimo (Kruskal){Colors.RESET} ---")
minimum_spanning_tree = sw_graph.kruskal()
total_weight = 0
print(f"El árbol de expansión mínimo que conecta a los personajes es:")
for edge in minimum_spanning_tree:
    origin, dest, weight = edge # Desempaquetar la tupla de la arista
    total_weight += weight
    print(f"  {Colors.CYAN}{origin.ljust(15)}{Colors.RESET} <-> {Colors.CYAN}{dest.ljust(15)}{Colors.RESET} | Episodios: {Colors.MAGENTA}{weight}{Colors.RESET}")
print(f"{Colors.BOLD}Peso total del árbol de expansión mínimo:{Colors.RESET} {Colors.BOLD_YELLOW}{total_weight}{Colors.RESET}")

# c. Número máximo de episodios compartidos
print(f"\n--- {Colors.BOLD_BLUE}c. Máximo de episodios compartidos{Colors.RESET} ---")
max_weight = 0
max_edges = []
for vertex in sw_graph:
    for edge in vertex.edges:
        # Actualizar el máximo si se encuentra una arista con mayor peso
        if edge.weight > max_weight:
            max_weight = edge.weight
            max_edges = [(vertex.value, edge.value)]
        elif edge.weight == max_weight:
            # Evitar duplicados en grafo no dirigido (A-B y B-A)
            if (edge.value, vertex.value) not in max_edges:
                max_edges.append((vertex.value, edge.value))

print(f"El número máximo de episodios compartidos es: {Colors.BOLD_YELLOW}{max_weight}{Colors.RESET}")
print("Pares de personajes que coinciden con este número:")
for origin, dest in max_edges:
    print(f"  - {Colors.CYAN}{origin}{Colors.RESET} y {Colors.CYAN}{dest}{Colors.RESET}")

# d. Calcular el camino más corto desde C-3PO a R2-D2 y desde Yoda a Darth Vader.
print(f"\n--- {Colors.BOLD_BLUE}d. Camino más corto (Dijkstra){Colors.RESET} ---")

def find_and_print_path(graph, origin, destination):
    """
    Encuentra y muestra el camino más corto entre dos vértices utilizando
    los resultados del algoritmo de Dijkstra.
    """
    # Dijkstra devuelve una pila con los caminos desde el origen a todos los demás nodos
    path_stack = graph.dijkstra(origin)
    path_cost = None
    full_path = []
    
    # Reconstruir el camino desde el destino hacia el origen usando los predecesores
    current_dest = destination
    while path_stack.size() > 0:
        value = path_stack.pop()
        # Buscar el nodo destino actual en la pila de resultados
        if value[0] == current_dest:
            # Si es la primera vez que lo encontramos, guardamos el costo total
            if path_cost is None:
                path_cost = value[1]
            full_path.append(value[0])
            # Actualizamos el destino al predecesor para seguir reconstruyendo el camino
            current_dest = value[2] 
    
    full_path.reverse()
    print(f"Camino de {Colors.CYAN}{origin}{Colors.RESET} a {Colors.CYAN}{destination}{Colors.RESET}:")
    
    # Verificar si se encontró un camino válido (si el origen es el primer elemento)
    if full_path and full_path[0] == origin:
        print(f"  {Colors.MAGENTA}{' -> '.join(full_path)}{Colors.RESET}")
        print(f"  Costo total (episodios): {Colors.BOLD_YELLOW}{path_cost}{Colors.RESET}")
    else:
        print(f"  {Colors.RED}No se encontró un camino.{Colors.RESET}")

find_and_print_path(sw_graph, "C-3PO", "R2-D2")
print()
find_and_print_path(sw_graph, "Yoda", "Darth Vader")

# e. Indicar qué personajes aparecieron en los nueve episodios de la saga.
print(f"\n--- {Colors.BOLD_BLUE}e. Personajes que aparecen en los 9 episodios de la saga{Colors.RESET} ---")
for vertex in sw_graph:
    if vertex.other_values and len(vertex.other_values.get("episodes", [])) == 9:
        print(f"  - {Colors.CYAN}{vertex.value}{Colors.RESET}")
