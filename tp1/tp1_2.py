def main(criaturas: list[tuple[int, int]]) -> tuple[list[int, int], int]:
    criaturas_ordenadas = sorted(criaturas, key=lambda c: (c[0], -c[1]))
    
    invictas = resolver_combates(criaturas_ordenadas)

    return (invictas, len(invictas))

def combinar_soluciones(izquierda: list[tuple[int, int]], derecha: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not izquierda:
        return derecha
    if not derecha:
        return izquierda
    atk_min = min(criatura[0] for criatura in derecha)
    def_max = max(criatura[1] for criatura in derecha)
    izquierda_filtrados = [criatura for criatura in izquierda if criatura[0] == atk_min or criatura[1] > def_max]  
    return izquierda_filtrados + derecha


def resolver_combates(criaturas: list[tuple[int, int]]) -> list[tuple[int, int]]:
    n = len(criaturas)
    if n <= 1:
        return criaturas

    mitad = n // 2
    izquierda = resolver_combates(criaturas[:mitad])
    derecha = resolver_combates(criaturas[mitad:])
    return combinar_soluciones(izquierda, derecha)