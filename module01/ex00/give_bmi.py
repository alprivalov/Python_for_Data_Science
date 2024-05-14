import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    retourne une liste de valeurs de l'Indice de Masse Corporelle (IMC).
    """
    bmi = list()
    for i in range(len(height)):
        bmi.append(weight[i]/(height[i] * height[i]))
    return bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    prend une liste d'IMC et une limite(en valeur numérique) en entrée,
    et retourne une liste de booléens indiquant si chaque IMC est supérieur à la limite.
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