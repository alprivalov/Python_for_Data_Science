import matplotlib.pyplot as plt
import pandas as pd


def clean_value(value):
    """
1.  Prend une liste flatte en params
2.  Fonction pour supprimer les suffixes "M" et "K" et convertir en nombre
3.  Return float(value[:-1]) * 1e6  # return un nombre convertir en millions
4.  Return float(value[:-1]) * 1e3  # return un nombre convertir en milliers
    """
    if value.endswith('M'):
        return float(value[:-1]) * 1e6
    elif value.endswith('K'):
        return float(value[:-1]) * 1e3
    else:
        return float(value)


def aff_pop(data: pd.DataFrame):
    """
1.  Recuperer les donnees francaise et belgique dans la data
2.  edit le x,y labels
3.  creation de l'axe y avec une liste de comprehension avec les donnees
4.  creation l'axe x sur les annee francaise
5.  indication des ticks a l'axe x et une limitation
6.  creation de laxe y pour laffichage : 2 * 1e7 ,4 * 1e7 ,6 * 1e7
7.  set les yticks sous format "M" de la liste comprehension cree
    """
    france = data[data["country"] == "France"]
    Belgium = data[data["country"] == "Belgium"]

    plt.xlabel("Year")
    plt.ylabel("Life expectancy")

    bl_data = [clean_value(value)
               for value in Belgium.values.flatten().tolist()[1:]]
    fr_data = [clean_value(value)
               for value in france.values.flatten().tolist()[1:]]
    years = france.columns[1:].values.astype(int)
    plt.plot(years, bl_data, "b", label="Belgium")
    plt.plot(years, fr_data, "g", label="France")

    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2040)

    max_pop = max(max(bl_data), max(fr_data))
    print(max_pop)
    y_ticks = [i * 1e7 for i in range(2, int(max_pop/1e7) + 1, 2)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])

    plt.legend()
    plt.show()
