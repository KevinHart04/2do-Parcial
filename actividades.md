# Actividades del Segundo Parcial

## Ejercicio 1: Pokédex con Árboles

Se tienen los datos de **1025 Pokémons** de las 9 generaciones, cargados de manera aleatoria. De cada Pokémon se conoce su nombre, número, tipo/s, debilidad/es, si tiene megaevolución (booleano) y si tiene forma Gigamax (booleano).

Se deben construir tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:

- Los índices de cada uno de los árboles deben ser **nombre**, **número** y **tipo**.
- Mostrar todos los datos de un Pokémon a partir de su **número** y **nombre**. Para este último, la búsqueda debe ser por proximidad (ej: si se busca “bul”, se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres).
- Mostrar todos los nombres de los Pokémons de un determinado tipo: **Fantasma**, **Fuego**, **Acero** y **Eléctrico**.
- Realizar un listado en orden ascendente por **número** y **nombre** de Pokémon, y además un listado por nivel por nombre.
- Mostrar todos los Pokémons que son débiles frente a **Jolteon**, **Lycanroc** y **Tyrantrum**.
- Mostrar todos los tipos de Pokémons y cuántos hay de cada tipo.
- Determinar cuántos Pokémons tienen **megaevolución**.
- Determinar cuántos Pokémons tienen forma **Gigamax**.

---

## Ejercicio 2: Grafo de Star Wars

Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:

- Cada vértice debe almacenar el nombre de un personaje. Las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan.
- Hallar el árbol de expansión mínimo desde el vértice que contiene a: **C-3PO**, **Yoda** y **Leia**.
- Determinar cuál es el número máximo de episodios que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número.
- Cargar al menos los siguientes personajes:
  - Luke Skywalker
  - Darth Vader
  - Yoda
  - Boba Fett
  - C-3PO
  - Leia
  - Rey
  - Kylo Ren
  - Chewbacca
  - Han Solo
  - R2-D2
  - BB-8
- Calcular el camino más corto desde **C-3PO** a **R2-D2** y desde **Yoda** a **Darth Vader**.
- Indicar qué personajes aparecieron en los nueve episodios de la saga.
