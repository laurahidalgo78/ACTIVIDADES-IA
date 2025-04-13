import heapq
from typing import List, Dict, Tuple, Optional, Set

class BaseConocimiento:
    def __init__(self):
        self.grafo = {
            'A': {'B': (5, 'L1'), 'C': (10, 'L2')},
            'B': {'A': (5, 'L1'), 'D': (8, 'L1'), 'E': (7, 'L3')},
            'C': {'A': (10, 'L2'), 'F': (12, 'L2')},
            'D': {'B': (8, 'L1'), 'G': (6, 'L1')},
            'E': {'B': (7, 'L3'), 'G': (9, 'L3'), 'H': (11, 'L4')},
            'F': {'C': (12, 'L2'), 'H': (4, 'L4')},
            'G': {'D': (6, 'L1'), 'E': (9, 'L3'), 'I': (5, 'L1')},
            'H': {'E': (11, 'L4'), 'F': (4, 'L4'), 'I': (8, 'L4')},
            'I': {'G': (5, 'L1'), 'H': (8, 'L4')}
        }
        
        self.reglas = {
            'min_transbordos': True,
            'max_comodidad': False,
            'evitar_lineas': []
        }

    def obtener_vecinos(self, estacion: str) -> Dict[str, Tuple[int, str]]:
        return self.grafo.get(estacion, {})

class PlanificadorRutas:
    def __init__(self, base_conocimiento: BaseConocimiento):
        self.bc = base_conocimiento
    
    def encontrar_ruta_optima(self, origen: str, destino: str) -> Optional[Tuple[List[str], int]]:
        cola_prioridad = []
        heapq.heappush(cola_prioridad, (0, origen, [], None))
        
        visitados: Set[str] = set()
        
        while cola_prioridad:
            costo_total, estacion_actual, ruta, linea_anterior = heapq.heappop(cola_prioridad)
            
            if estacion_actual == destino:
                ruta_completa = [origen]
                for est, _ in ruta:
                    ruta_completa.append(est)
                return ruta_completa, costo_total
                
            if estacion_actual in visitados:
                continue
                
            visitados.add(estacion_actual)
            
            for vecino, (tiempo, linea) in self.bc.obtener_vecinos(estacion_actual).items():
                if vecino in visitados:
                    continue
                    
                nueva_ruta = ruta.copy()
                nueva_ruta.append((vecino, linea))
                
                # Cálculo de costos simplificado
                costo_adicional = 0
                if linea_anterior and linea_anterior != linea:
                    costo_adicional += 10  # Penalización por transbordo
                if linea in self.bc.reglas['evitar_lineas']:
                    costo_adicional += 15
                
                heapq.heappush(cola_prioridad, 
                             (costo_total + tiempo + costo_adicional, 
                              vecino, 
                              nueva_ruta, 
                              linea))
        
        return None

def main():
    print("Sistema Inteligente de Planificación de Rutas")
    print("Estaciones disponibles: A, B, C, D, E, F, G, H, I\n")
    
    bc = BaseConocimiento()
    planificador = PlanificadorRutas(bc)
    
    # Configuración simple sin inputs para prueba inicial
    origen = 'A'
    destino = 'I'
    print(f"Calculando ruta desde {origen} hasta {destino}...")
    
    resultado = planificador.encontrar_ruta_optima(origen, destino)
    
    if resultado:
        ruta, costo = resultado
        print(f"\nRuta encontrada: {' → '.join(ruta)}")
        print(f"Tiempo total estimado: {costo} minutos")
    else:
        print("\nNo se encontró ruta válida")

if __name__ == "__main__":
    main()