def main(criaturas: list[tuple[int, int]]) -> tuple[list[int, int], int]:
    frente_activo = sorted(criaturas, key=lambda c: (c[0], -c[1]))
    
    invictas = resolver_invictos(frente_activo)

    return (invictas, len(invictas))

def combinar_frentes(izquierda: list[tuple[int, int]], derecha: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not izquierda:
        return derecha
    if not derecha:
        return izquierda

    y_max = max(criatura[1] for criatura in derecha)
    izquierda_filtrados = [criatura for criatura in izquierda if criatura[1] > y_max]  
    return izquierda_filtrados + derecha


def resolver_invictos(frente_activo: list[tuple[int, int]]) -> list[tuple[int, int]]:
    n = len(frente_activo)
    if n <= 1:
        return frente_activo

    mitad = n // 2
    izquierda = resolver_invictos(frente_activo[:mitad])
    derecha = resolver_invictos(frente_activo[mitad:])
    return combinar_frentes(izquierda, derecha)