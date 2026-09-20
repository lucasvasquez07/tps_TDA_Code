import os

def parsear_archivo(filepath: str) -> tuple[int, list[set[int]]]:
    """
    Lee el archivo de entrada en formato 'p n m' y 'e u v'.
    Retorna la cantidad de prendas  y la lista de adyacencias.
    """
    if not os.path.exists(filepath):
        return 0, []
        
    with open(filepath, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        
    cantidad_prendas = 0
    grafo = []
    
    for linea in lineas:
        linea = linea.strip()
        if not linea:
            continue
        partes = linea.split()
        if partes[0] == 'p':
            cantidad_prendas = int(partes[1])
            grafo = [set() for _ in range(cantidad_prendas + 1)]
        elif partes[0] == 'e':
            u, v = int(partes[1]), int(partes[2])
            if 1 <= u <= cantidad_prendas and 1 <= v <= cantidad_prendas:
                grafo[u].add(v)
                grafo[v].add(u)
                
    return cantidad_prendas, grafo


def es_valido(prenda: int, lavarropas: int, grafo: list[set[int]], asignacion: list[int]) -> bool:
    """
    Verifica si la prenda puede asignarse al lavarropas sin entrar en conflicto
    con prendas vecinas (incompatibles) ya asignadas.
    """
    for vecino in grafo[prenda]:
        if asignacion[vecino] == lavarropas:
            return False
    return True


def resolver_lavarropas(cantidad_prendas: int, grafo: list[set[int]]) -> list[tuple[int, str]]:
    """
    Resuelve el armado de lavarropas (Coloreo de Grafos) minimizando la cantidad de lavarropas.
    """
    if cantidad_prendas == 0:
        return []

    # Ordenar prendas por grado descendente de incompatibilidad
    prendas_sorted = sorted(range(1, cantidad_prendas + 1), key=lambda x: len(grafo[x]), reverse=True)

    asignacion = [0] * (cantidad_prendas + 1)
    min_cantidad_lavarropas_necesarios_hallada = cantidad_prendas + 1
    mejor_asignacion = [0] * (cantidad_prendas + 1)

    def backtracking(idx: int, cant_lavarropas_rama: int):
        nonlocal min_cantidad_lavarropas_necesarios_hallada, mejor_asignacion

        # Poda por Acotamiento
        if cant_lavarropas_rama >= min_cantidad_lavarropas_necesarios_hallada:
            return

        # Caso Base: Se asignaron todas las prendas exitosamente
        if idx == len(prendas_sorted):
            min_cantidad_lavarropas_necesarios_hallada = cant_lavarropas_rama
            mejor_asignacion = asignacion.copy()
            return

        prenda = prendas_sorted[idx]

        # Poda por Simetría: probar lavarropas en uso + a lo sumo 1 nuevo
        for lavarropas in range(1, cant_lavarropas_rama + 2):
            if es_valido(prenda, lavarropas, grafo, asignacion):
                asignacion[prenda] = lavarropas
                
                backtracking(idx + 1, max(cant_lavarropas_rama, lavarropas))
                
                asignacion[prenda] = 0  # Backtrack

    backtracking(0, 0)

    # Convertir números de lavarropas a etiquetas string ("A", "B", "C", ...)
    def obtener_etiqueta(c: int) -> str:
        if 1 <= c <= 26:
            return chr(ord('A') + c - 1)
        return str(c)

    resultado = [(i, obtener_etiqueta(mejor_asignacion[i])) for i in range(1, cantidad_prendas + 1)]
    return resultado


def main(filepath: str) -> list[tuple[int, str]]:
    cantidad_prendas, grafo = parsear_archivo(filepath)
    return resolver_lavarropas(cantidad_prendas, grafo)