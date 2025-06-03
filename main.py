import time, random

#creación de lista 
lista = [random.randint(0, 1000) for i in range(20000)]
#elección de un valor que se sabe que existe en la lista
elemento = random.choice(lista)

#Algoritmo Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Búsqueda lineal
def busqueda_lineal(arr, valor):
    for i in range(len(arr)):
        if arr[i] == valor:
            return i, arr[i]
    return -1

# Búsqueda binaria
def busqueda_binaria(arr, valor):
    izquierda = 0
    derecha = len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == valor:
            return medio, arr[medio]
        elif arr[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Búsqueda lineal en lista desordenada
# se utiliza el metodo time para medir el tiempo desde el comienzo
# hasta finalizar el proceso.
inicio_lineal = time.time()
elemento_lineal = busqueda_lineal(lista, elemento)
fin_lineal = time.time()

# Ordenar la lista
#se utiliza el metodo sort, para identificar la variabilidad de tiempo entre
#diferentes volúmenes de datos
inicio_sort = time.time()
lista_ordenado = bubble_sort(lista)
fin_sort = time.time()

# Búsqueda binaria en lista ordenada
# se utiliza el mismo metodo para medir el tiempo de ejecución
inicio_binaria = time.time()
elemento_binario = busqueda_binaria(lista_ordenado, elemento)
fin_binaria = time.time()

# Se imprimen los resultados de los tiempos de ejecución
print(f"Volúmen de datos: {len(lista)}, Elemento a buscar: {elemento}")
print(f"Ordenamiento por búrbuja: {fin_sort - inicio_sort:.6f} segundos")
print(f"Búsqueda lineal (lista desordenada): indice: {elemento_lineal[0]}, Valor encontrado: {elemento_lineal[1]}, {fin_lineal - inicio_lineal:.6f} segundos")
print(f"Búsqueda binaria (lista ordenada): indice: {elemento_binario[0]}, Valor encontrado: {elemento_binario[1]}, {fin_binaria - inicio_binaria:.6f} segundos")