def main(criaturas: list[tuple[int, int]]) -> tuple[list[int, int], int]:
    criaturas_ordenadas = ordenar_criaturas(criaturas)
    
    invictas = resolver_combates(criaturas_ordenadas)

    return (invictas, len(invictas))

def combinar_soluciones(izquierda: list[tuple[int, int]], derecha: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not izquierda:
        return derecha
    if not derecha:
        return izquierda
    atk_min = derecha[0][0]
    def_max = max(criatura[1] for criatura in derecha)
    izquierda_filtrados = [criatura for criatura in izquierda if criatura[1] > def_max or (criatura[1]>= def_max and criatura[0] == atk_min)]
    return izquierda_filtrados + derecha


def resolver_combates(criaturas: list[tuple[int, int]]) -> list[tuple[int, int]]:
    n = len(criaturas)
    if n <= 1:
        return criaturas

    mitad = n // 2
    izquierda = resolver_combates(criaturas[:mitad])
    derecha = resolver_combates(criaturas[mitad:])
    return combinar_soluciones(izquierda, derecha)


def ordenar_criaturas(criaturas):
    """Ordena por ataque de manera ascendente y, en caso de empate, por defensa descendente."""
    if len(criaturas) <= 1:
        return criaturas

    medio = len(criaturas) // 2

    izquierda = ordenar_criaturas(criaturas[:medio])
    derecha = ordenar_criaturas(criaturas[medio:])

    return merge(izquierda, derecha)


def merge(izquierda, derecha):
    ordenados = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i][0] < derecha[j][0]:
            ordenados.append(izquierda[i])
            i += 1
        elif izquierda[i][0] > derecha[j][0]:
            ordenados.append(derecha[j])
            j += 1
        else:
            if izquierda[i][1] >= derecha[j][1]:
                ordenados.append(izquierda[i])
                i += 1
            else:
                ordenados.append(derecha[j])
                j += 1

    ordenados.extend(izquierda[i:])
    ordenados.extend(derecha[j:])

    return ordenados
