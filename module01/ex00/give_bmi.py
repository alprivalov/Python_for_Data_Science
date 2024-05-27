

def give_bmi(
        height: list[int | float],
        weight: list[int | float]) -> list[int | float]:
    """
1.  Retourne une liste de valeurs de l'Indice de Masse Corporelle (IMC).
    """
    bmi = list()
    for i in range(len(height)):
        bmi.append(weight[i]/(height[i] * height[i]))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
1.  Prend une liste d'IMC et une limite(en valeur numerique) en entrée,
2.  Indique si chaque IMC est superieur a la limite.
3.  Retourne une liste de booleens
    """
    result = list()
    for i in bmi:
        if i > limit:
            result.append(True)
        else:
            result.append(False)
    return result


def main():
    return 0


if __name__ == "__main__":
    main()
