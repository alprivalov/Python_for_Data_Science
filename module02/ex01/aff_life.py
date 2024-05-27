import pandas as pd
import matplotlib.pyplot as plt


def aff_life(data: pd.DataFrame):
    """
1.  Charge la dataFrame
2.  Edit le label x, y
3.  Charge la data Francaise dans le plot
4.  Changement l'axe a tout les 40 ans
    """
    france = data[data["country"] == "France"]
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.title("France Life expectancy Projections")
    plt.plot(
        france.columns[1:].values.flatten(),
        france.iloc[0:, 1:].values.flatten())
    plt.xticks(france.columns[1::40])
    plt.show()
