<h1 class="text-center">Actividad 2 - Búsqueda y sistemas basados en reglas</h1>
<h3>Estudiantes: Mabell Tatiana Jimenez Reyes, Valeria Stefany Rojas Sanchez y Laura Valentina Hidalgo Melo</h3>

Este código implementa un sistema de planificación de rutas para transporte masivo (como transmilenio), utilizando un enfoque basado en grafos ponderados y el algoritmo de Dijkstra para encontrar la mejor ruta entre dos estaciones, teniendo en cuenta que:

- Tiempos de viaje entre estaciones. <br>
- Penalizaciones por transbordos. <br>
- Preferencias personalizables.

<h3>🔍 Componentes Principales</h3>
1. Base de Conocimiento (BaseConocimiento) <br>
 <br>- Grafo de conexiones: <br>
   <br>- Modela las estaciones como nodos y los trayectos como aristas con: <br>
   - Tiempo de viaje (ej. 'A' → 'B': 5 minutos). <br>
   - Línea de transporte (ej. 'L1'). <br>
- Reglas de preferencia: <br>
   - min_transbordos: Prioriza rutas con menos cambios de línea. <br>
   - evitar_lineas: Lista de líneas no deseadas (ej. ['L3']). <br>
