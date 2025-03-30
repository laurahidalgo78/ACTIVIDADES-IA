<h1 class="text-center">Actividad 2 - Búsqueda y sistemas basados en reglas</h1>
<h3>Estudiantes: Mabell Tatiana Jimenez Reyes, Valeria Stefany Rojas Sanchez y Laura Valentina Hidalgo Melo</h3>

Este código implementa un sistema de planificación de rutas para transporte masivo (como transmilenio), utilizando un enfoque basado en grafos ponderados y el algoritmo de Dijkstra para encontrar la mejor ruta entre dos estaciones, teniendo en cuenta que:

- Tiempos de viaje entre estaciones. <br>
- Penalizaciones por transbordos. <br>
- Preferencias personalizables.

## 🔍 Componentes Principales

### 1. Base de Conocimiento (BaseConocimiento)

#### 📌 Grafo de conexiones:
Modela las estaciones como nodos y los trayectos como aristas con:
- ⏳ **Tiempo de viaje**: Ejemplo: `A → B`: 5 minutos.
- 🚇 **Línea de transporte**: Ejemplo: `L1`.

#### ⚙️ Reglas de preferencia:
- 🔄 **min_transbordos**: Prioriza rutas con menos cambios de línea.
- 🚫 **evitar_lineas**: Lista de líneas no deseadas. Ejemplo: `['L3']`.
### 2. Algoritmo de Búsqueda (PlanificadorRutas)

#### 🛤️ Método de búsqueda:
El algoritmo utilizado es una variante modificada de **Dijkstra**, implementado con una **cola de prioridad (heapq)**. Su objetivo principal es encontrar la ruta con el **menor costo total**, considerando tanto el tiempo de viaje como penalizaciones adicionales.

#### ⚠️ Penalizaciones:
Para ajustar las rutas y evitar opciones menos deseables, se aplican las siguientes penalizaciones:

- 🔄 **+10 puntos** por cada **transbordo** (cambio de línea).
- 🚫 **+15 puntos** si la línea pertenece a la lista `evitar_lineas`.

Este sistema permite priorizar rutas más eficientes y minimizar cambios innecesarios en el trayecto.


