import random

# Representamos estaciones y sus coordenadas (tiempos totales a otras)
estaciones = {
    'A': [0, 5, 10],
    'B': [5, 0, 7],
    'C': [10, 12, 0],
    'D': [8, 0, 6],
    'E': [7, 9, 11],
    'F': [12, 0, 4],
    'G': [6, 9, 5],
    'H': [11, 4, 8],
    'I': [5, 8, 0]
}

# Convertimos estaciones en lista para acceso por índice
nombres_estaciones = list(estaciones.keys())
datos = list(estaciones.values())

# Función para calcular distancia euclidiana
def distancia(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

# K-means simple
def k_means(datos, k=3, iteraciones=10):
    # Inicializamos centros al azar
    centros = random.sample(datos, k)
    
    for _ in range(iteraciones):
        clusters = [[] for _ in range(k)]
        
        # Asignar puntos al centro más cercano
        for i, punto in enumerate(datos):
            distancias = [distancia(punto, centro) for centro in centros]
            indice_cercano = distancias.index(min(distancias))
            clusters[indice_cercano].append(i)
        
        # Recalcular centros
        for i in range(k):
            if clusters[i]:
                suma = [0] * len(datos[0])
                for indice in clusters[i]:
                    for j in range(len(datos[0])):
                        suma[j] += datos[indice][j]
                centros[i] = [x / len(clusters[i]) for x in suma]
    
    return clusters

# Ejecutar clustering
clusters = k_means(datos)

# Mostrar resultados
print("Resultado del agrupamiento (Clustering no supervisado):")
for i, cluster in enumerate(clusters):
    estaciones_en_cluster = [nombres_estaciones[j] for j in cluster]
    print(f"Grupo {i+1}: {', '.join(estaciones_en_cluster)}")
