# Trabajo práctico de integración

Tema: Algoritmos de Búsqueda y Ordenamiento.
Materia: Programación 1
Profesor: Bruselario, Sebastian.
Alumnos:
Ayala, Nahuel.
Archiria, Facundo Miguel.

# Caso Práctico

Se desarrolló un programa en Python con el objetivo de analizar el impacto del ordenamiento sobre la eficiencia de los algoritmos de búsqueda. Se generó una lista de números aleatorios y se aplico el algoritmo de ordenamiento Bubble sort. Luego se evalúo los dos algoritmos de búsqueda: búsqueda lineal sobre la lista desordenada y búsqueda binaria sobre la lista ordenada.
Se midió el tiempo de ejecución de cada uno utilizando la librería time, buscando comparar el rendimiento de cada método para localizar un mismo elemento dentro de la lista.

# Funcionamiento

Para simular diferentes escenarios y obtener resultados variados para su posterior análisis, se debe modificar el parametro del metodo range() en la linea 4 del código, lo que permite ajustar el volumen de datos generado.

# Resultados esperados

Por cada ejecución se imprime en la terminal los siguientes datos:

- El volumen de datos generado y el elemento a buscar.
- El tiempo de ejecución del algoritmo de ordenamiente Bubble Sort.
- El resultado de la búsqueda lineal, detallando el índice encontrado, valor y tiempo de ejecución.
- El resultado de la búsqueda binaria, detallando el índice encontrado, valor y tiempo de ejecución.
