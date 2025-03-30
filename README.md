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

## 📌 Conclusión del Código

Este programa implementa un sistema inteligente de planificación de rutas basado en un **grafo ponderado**, donde las estaciones están conectadas por diferentes líneas de transporte.  
Utiliza un algoritmo de búsqueda con **cola de prioridad** (basado en *Dijkstra*) para encontrar la ruta más eficiente entre dos estaciones, considerando penalizaciones por cambios de línea (*transbordos*).

### 🔹 Principales Características:
✔ **Modelo de datos estructurado**: Usa un diccionario (`self.grafo`) para representar las conexiones entre estaciones y otro (`self.reglas`) para definir restricciones en la búsqueda.  
✔ **Algoritmo eficiente**: Implementa una búsqueda basada en prioridad con `heapq`, garantizando la mejor ruta en términos de tiempo.  
✔ **Gestión de reglas personalizadas**: Permite establecer restricciones como **minimizar transbordos** o **evitar ciertas líneas**.  
✔ **Interfaz sencilla**: `main()` define el flujo del programa, permitiendo ejecutar consultas de rutas y mostrando resultados de manera clara.  

### 🔹 Aplicaciones y Usos Potenciales:
✅ **Planificación de rutas** en sistemas de transporte público (*trenes, autobuses, metro*).  
✅ **Optimización de tiempos de viaje** en redes de logística y distribución.  
✅ **Implementación en sistemas de navegación y GPS**.  

En resumen, este código es una implementación **básica pero poderosa** de un sistema de búsqueda de rutas óptimas, **adaptable a diferentes contextos** y **escalable** con nuevas funcionalidades como tiempos en tiempo real o múltiples criterios de optimización. 🚀

- 🔄 **+10 puntos** por cada **transbordo** (cambio de línea).
- 🚫 **+15 puntos** si la línea pertenece a la lista `evitar_lineas`.

Este sistema permite priorizar rutas más eficientes y minimizar cambios innecesarios en el trayecto.


