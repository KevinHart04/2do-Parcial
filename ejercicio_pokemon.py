from tree import BinaryTree
from console_colors import Colors

# Datos de 50 Pokémon para el ejercicio
pokemon_data = [
    {"number": 1, "name": "Bulbasaur", "types": ["Grass", "Poison"], "weaknesses": ["Fire", "Ice", "Flying", "Psychic"], "has_mega": False, "has_gigantamax": True},
    {"number": 4, "name": "Charmander", "types": ["Fire"], "weaknesses": ["Water", "Ground", "Rock"], "has_mega": False, "has_gigantamax": True},
    {"number": 7, "name": "Squirtle", "types": ["Water"], "weaknesses": ["Electric", "Grass"], "has_mega": False, "has_gigantamax": True},
    {"number": 25, "name": "Pikachu", "types": ["Electric"], "weaknesses": ["Ground"], "has_mega": False, "has_gigantamax": True},
    {"number": 131, "name": "Lapras", "types": ["Water", "Ice"], "weaknesses": ["Electric", "Grass", "Fighting", "Rock"], "has_mega": False, "has_gigantamax": True},
    {"number": 143, "name": "Snorlax", "types": ["Normal"], "weaknesses": ["Fighting"], "has_mega": False, "has_gigantamax": True},
    {"number": 6, "name": "Charizard", "types": ["Fire", "Flying"], "weaknesses": ["Water", "Electric", "Rock"], "has_mega": True, "has_gigantamax": True},
    {"number": 9, "name": "Blastoise", "types": ["Water"], "weaknesses": ["Electric", "Grass"], "has_mega": True, "has_gigantamax": True},
    {"number": 94, "name": "Gengar", "types": ["Ghost", "Poison"], "weaknesses": ["Ghost", "Psychic", "Dark"], "has_mega": True, "has_gigantamax": True},
    {"number": 150, "name": "Mewtwo", "types": ["Psychic"], "weaknesses": ["Bug", "Ghost", "Dark"], "has_mega": True, "has_gigantamax": False},
    {"number": 384, "name": "Rayquaza", "types": ["Dragon", "Flying"], "weaknesses": ["Ice", "Rock", "Dragon", "Fairy"], "has_mega": True, "has_gigantamax": False},
    {"number": 445, "name": "Garchomp", "types": ["Dragon", "Ground"], "weaknesses": ["Ice", "Dragon", "Fairy"], "has_mega": True, "has_gigantamax": False},
    {"number": 135, "name": "Jolteon", "types": ["Electric"], "weaknesses": ["Ground"], "has_mega": False, "has_gigantamax": False},
    {"number": 745, "name": "Lycanroc", "types": ["Rock"], "weaknesses": ["Water", "Grass", "Fighting", "Ground", "Steel"], "has_mega": False, "has_gigantamax": False},
    {"number": 697, "name": "Tyrantrum", "types": ["Rock", "Dragon"], "weaknesses": ["Ice", "Fighting", "Ground", "Steel", "Dragon", "Fairy"], "has_mega": False, "has_gigantamax": False},
    {"number": 37, "name": "Vulpix", "types": ["Fire"], "weaknesses": ["Water", "Ground", "Rock"], "has_mega": False, "has_gigantamax": False},
    {"number": 58, "name": "Growlithe", "types": ["Fire"], "weaknesses": ["Water", "Ground", "Rock"], "has_mega": False, "has_gigantamax": False},
    {"number": 77, "name": "Ponyta", "types": ["Fire"], "weaknesses": ["Water", "Ground", "Rock"], "has_mega": False, "has_gigantamax": False},
    {"number": 92, "name": "Gastly", "types": ["Ghost", "Poison"], "weaknesses": ["Ghost", "Psychic", "Dark"], "has_mega": False, "has_gigantamax": False},
    {"number": 93, "name": "Haunter", "types": ["Ghost", "Poison"], "weaknesses": ["Ghost", "Psychic", "Dark"], "has_mega": False, "has_gigantamax": False},
    {"number": 208, "name": "Steelix", "types": ["Steel", "Ground"], "weaknesses": ["Fire", "Water", "Fighting", "Ground"], "has_mega": True, "has_gigantamax": False},
    {"number": 306, "name": "Aggron", "types": ["Steel", "Rock"], "weaknesses": ["Fighting", "Ground", "Water"], "has_mega": True, "has_gigantamax": False},
    {"number": 100, "name": "Voltorb", "types": ["Electric"], "weaknesses": ["Ground"], "has_mega": False, "has_gigantamax": False},
    {"number": 101, "name": "Electrode", "types": ["Electric"], "weaknesses": ["Ground"], "has_mega": False, "has_gigantamax": False},
    {"number": 82, "name": "Magneton", "types": ["Electric", "Steel"], "weaknesses": ["Ground", "Fire", "Fighting"], "has_mega": False, "has_gigantamax": False},
    {"number": 125, "name": "Electabuzz", "types": ["Electric"], "weaknesses": ["Ground"], "has_mega": False, "has_gigantamax": False},
    {"number": 149, "name": "Dragonite", "types": ["Dragon", "Flying"], "weaknesses": ["Ice", "Rock", "Dragon", "Fairy"], "has_mega": False, "has_gigantamax": False},
    {"number": 151, "name": "Mew", "types": ["Psychic"], "weaknesses": ["Bug", "Ghost", "Dark"], "has_mega": False, "has_gigantamax": False},
    {"number": 248, "name": "Tyranitar", "types": ["Rock", "Dark"], "weaknesses": ["Fighting", "Ground", "Bug", "Steel", "Water", "Grass", "Fairy"], "has_mega": True, "has_gigantamax": False},
    {"number": 257, "name": "Blaziken", "types": ["Fire", "Fighting"], "weaknesses": ["Water", "Ground", "Flying", "Psychic"], "has_mega": True, "has_gigantamax": False},
    {"number": 3, "name": "Venusaur", "types": ["Grass", "Poison"], "weaknesses": ["Fire", "Ice", "Flying", "Psychic"], "has_mega": True, "has_gigantamax": True},
    {"number": 65, "name": "Alakazam", "types": ["Psychic"], "weaknesses": ["Bug", "Ghost", "Dark"], "has_mega": True, "has_gigantamax": False},
    {"number": 181, "name": "Ampharos", "types": ["Electric"], "weaknesses": ["Ground"], "has_mega": True, "has_gigantamax": False},
    {"number": 227, "name": "Skarmory", "types": ["Steel", "Flying"], "weaknesses": ["Fire", "Electric"], "has_mega": False, "has_gigantamax": False},
    {"number": 448, "name": "Lucario", "types": ["Fighting", "Steel"], "weaknesses": ["Fire", "Fighting", "Ground"], "has_mega": True, "has_gigantamax": False},
    {"number": 79, "name": "Slowpoke", "types": ["Water", "Psychic"], "weaknesses": ["Grass", "Electric", "Bug", "Ghost", "Dark"], "has_mega": False, "has_gigantamax": False},
    {"number": 144, "name": "Articuno", "types": ["Ice", "Flying"], "weaknesses": ["Rock", "Steel", "Fire", "Electric"], "has_mega": False, "has_gigantamax": False},
    {"number": 145, "name": "Zapdos", "types": ["Electric", "Flying"], "weaknesses": ["Ice", "Rock"], "has_mega": False, "has_gigantamax": False},
    {"number": 146, "name": "Moltres", "types": ["Fire", "Flying"], "weaknesses": ["Water", "Electric", "Rock"], "has_mega": False, "has_gigantamax": False},
    {"number": 243, "name": "Raikou", "types": ["Electric"], "weaknesses": ["Ground"], "has_mega": False, "has_gigantamax": False},
    {"number": 244, "name": "Entei", "types": ["Fire"], "weaknesses": ["Water", "Ground", "Rock"], "has_mega": False, "has_gigantamax": False},
    {"number": 245, "name": "Suicune", "types": ["Water"], "weaknesses": ["Grass", "Electric"], "has_mega": False, "has_gigantamax": False},
    {"number": 249, "name": "Lugia", "types": ["Psychic", "Flying"], "weaknesses": ["Electric", "Ice", "Rock", "Ghost", "Dark"], "has_mega": False, "has_gigantamax": False},
    {"number": 250, "name": "Ho-Oh", "types": ["Fire", "Flying"], "weaknesses": ["Rock", "Electric", "Water"], "has_mega": False, "has_gigantamax": False},
    {"number": 373, "name": "Salamence", "types": ["Dragon", "Flying"], "weaknesses": ["Ice", "Rock", "Dragon", "Fairy"], "has_mega": True, "has_gigantamax": False},
    {"number": 376, "name": "Metagross", "types": ["Steel", "Psychic"], "weaknesses": ["Ground", "Ghost", "Fire", "Dark"], "has_mega": True, "has_gigantamax": False},
    {"number": 475, "name": "Gallade", "types": ["Psychic", "Fighting"], "weaknesses": ["Flying", "Ghost", "Fairy"], "has_mega": True, "has_gigantamax": False},
    {"number": 483, "name": "Dialga", "types": ["Steel", "Dragon"], "weaknesses": ["Fighting", "Ground"], "has_mega": False, "has_gigantamax": False},
    {"number": 484, "name": "Palkia", "types": ["Water", "Dragon"], "weaknesses": ["Dragon", "Fairy"], "has_mega": False, "has_gigantamax": False},
    {"number": 487, "name": "Giratina", "types": ["Ghost", "Dragon"], "weaknesses": ["Ghost", "Dragon", "Ice", "Dark", "Fairy"], "has_mega": False, "has_gigantamax": False},
]

# Crear los tres árboles
name_tree = BinaryTree()
number_tree = BinaryTree()
type_tree = BinaryTree()

# Poblar los árboles
for pokemon in pokemon_data:
    name_tree.insert(pokemon['name'], pokemon)
    number_tree.insert(pokemon['number'], pokemon)
    for p_type in pokemon['types']:
        type_node = type_tree.search(p_type)
        if type_node:
            type_node.other_values.append(pokemon['name'])
        else:
            type_tree.insert(p_type, [pokemon['name']])

print(f"{Colors.BOLD_GREEN}Árboles creados y poblados con 50 Pokémon.{Colors.RESET}")

# --- Resolución de los puntos del ejercicio ---

# a. Mostrar datos por número y nombre (proximidad)
print(f"\n--- {Colors.BOLD_BLUE}a. Búsqueda de Pokémon{Colors.RESET} ---")
num_to_find = 25
print(f"\nBuscando Pokémon con número {Colors.BOLD_YELLOW}{num_to_find}{Colors.RESET}:")
node = number_tree.search(num_to_find)
if node:
    pokemon = node.other_values
    print(f"  {Colors.CYAN}Nombre:{Colors.RESET} {Colors.MAGENTA}{pokemon['name']} (#{pokemon['number']}){Colors.RESET}")
    print(f"  {Colors.CYAN}Tipos:{Colors.RESET} {Colors.MAGENTA}{', '.join(pokemon['types'])}{Colors.RESET}")
    print(f"  {Colors.CYAN}Debilidades:{Colors.RESET} {Colors.MAGENTA}{', '.join(pokemon['weaknesses'])}{Colors.RESET}")
    print(f"  {Colors.CYAN}Megaevolución:{Colors.RESET} {Colors.MAGENTA}{' Sí' if pokemon['has_mega'] else ' No'}{Colors.RESET}")
    print(f"  {Colors.CYAN}Gigamax:{Colors.RESET} {Colors.MAGENTA}{' Sí' if pokemon['has_gigantamax'] else ' No'}{Colors.RESET}")

name_to_find = "Char"
print(f"\nBuscando Pokémon cuyos nombres comienzan con {Colors.BOLD_YELLOW}'{name_to_find}'{Colors.RESET}:")

def get_proximity_results(root, value, results):
    if root is not None:
        if root.value.startswith(value):
            results.append(root.value)
        get_proximity_results(root.left, value, results)
        get_proximity_results(root.right, value, results)

proximity_list = []
get_proximity_results(name_tree.root, name_to_find, proximity_list)
print(f"{Colors.MAGENTA}{', '.join(proximity_list)}{Colors.RESET}")

# b. Mostrar nombres de Pokémon de tipos específicos
print(f"\n--- {Colors.BOLD_BLUE}b. Listado por tipos específicos{Colors.RESET} ---")
types_to_list = ["Ghost", "Fire", "Steel", "Electric"]
for p_type in types_to_list:
    node = type_tree.search(p_type)
    if node:
        print(f"  {Colors.BOLD_CYAN}{p_type}:{Colors.RESET} {Colors.MAGENTA}{', '.join(node.other_values)}{Colors.RESET}")

# c. Listados en orden ascendente y por nivel
print(f"\n--- {Colors.BOLD_BLUE}c. Listados ordenados{Colors.RESET} ---")

def get_in_order_data(root, data_list):
    if root is not None:
        get_in_order_data(root.left, data_list)
        data_list.append((root.value, root.other_values))
        get_in_order_data(root.right, data_list)

print(f"\n{Colors.BOLD}Listado por Número (ascendente):{Colors.RESET}")
num_list = []
get_in_order_data(number_tree.root, num_list)
for num, data in num_list:
    print(f"  {Colors.CYAN}#{str(num).ljust(4)}{Colors.RESET} {Colors.MAGENTA}{data['name']}{Colors.RESET}")

print(f"\n{Colors.BOLD}Listado por Nombre (ascendente):{Colors.RESET}")
name_list = []
get_in_order_data(name_tree.root, name_list)
for name, data in name_list:
    print(f"  {Colors.CYAN}{name.ljust(15)}{Colors.RESET} {Colors.MAGENTA}#{data['number']}{Colors.RESET}")

print(f"\n{Colors.BOLD}Listado por nivel (por nombre):{Colors.RESET}")
name_tree.by_level() # by_level ya imprime, lo dejamos así por simplicidad

# d. Mostrar Pokémon débiles a Jolteon, Lycanroc y Tyrantrum
print(f"\n--- {Colors.BOLD_BLUE}d. Pokémon débiles contra Jolteon, Lycanroc y Tyrantrum{Colors.RESET} ---")

def get_pokemon_types(tree, name):
    node = tree.search(name)
    if node:
        return node.other_values['types']
    return []

target_pokemon_names = ["Jolteon", "Lycanroc", "Tyrantrum"]
target_types = set()
for p_name in target_pokemon_names:
    types = get_pokemon_types(name_tree, p_name)
    target_types.update(types)

print(f"Tipos de ataque a considerar (de {', '.join(target_pokemon_names)}): {Colors.BOLD_YELLOW}{', '.join(target_types)}{Colors.RESET}")
 
weak_pokemon = []
def find_weak_pokemon(root):
    if root is not None:
        find_weak_pokemon(root.left)
        if any(weakness in target_types for weakness in root.other_values['weaknesses']):
            weak_pokemon.append(root.value)
        find_weak_pokemon(root.right)

find_weak_pokemon(name_tree.root)
print(f"\n{Colors.BOLD}Pokémon que son débiles contra alguno de ellos:{Colors.RESET}")
print(f"{Colors.MAGENTA}{', '.join(weak_pokemon)}{Colors.RESET}")

# e. Mostrar todos los tipos y cuántos hay de cada uno
print(f"\n--- {Colors.BOLD_BLUE}e. Conteo de Pokémon por tipo{Colors.RESET} ---")

def get_types_count(root, type_list):
    if root is not None:
        get_types_count(root.left, type_list)
        type_list.append((root.value, len(root.other_values)))
        get_types_count(root.right, type_list)

types_count_list = []
get_types_count(type_tree.root, types_count_list)
for p_type, count in sorted(types_count_list, key=lambda item: item[1], reverse=True):
    print(f"  {Colors.CYAN}{p_type.ljust(10)}{Colors.RESET} - {Colors.MAGENTA}{count} Pokémon{Colors.RESET}")

# f. Determinar cuántos Pokémon tienen megaevolución
print(f"\n--- {Colors.BOLD_BLUE}f. y g. Conteos de Evoluciones Especiales{Colors.RESET} ---")

def count_special_forms(root, counts):
    if root is not None:
        count_special_forms(root.left, counts)
        if root.other_values['has_mega']:
            counts['mega'] += 1
        if root.other_values['has_gigantamax']:
            counts['gigantamax'] += 1
        count_special_forms(root.right, counts)

special_counts = {'mega': 0, 'gigantamax': 0}
count_special_forms(name_tree.root, special_counts)

print(f"  {Colors.CYAN}Pokémon con Megaevolución:{Colors.RESET} {Colors.MAGENTA}{special_counts['mega']}{Colors.RESET}")
print(f"  {Colors.CYAN}Pokémon con forma Gigamax:{Colors.RESET} {Colors.MAGENTA}{special_counts['gigantamax']}{Colors.RESET}")

