from load_csv import load
import matplotlib.pyplot as plt
import pandas as ps


def projection_life(
        data_income: ps.DataFrame, data_life_expectancy: ps.DataFrame):
    """
1.  On load la data depuis les fichier csv
2.  On extrait les donner avec data_income["1900"] avec une date precise
3.  On charge les donner dans un plot sous format 'o' pour avoir des points
4.  On nomme les label et le titre
5.  On scale l'axe x et on applique un courbe logarithmique
    """
    global_income = data_income["1900"]
    global_life = data_life_expectancy["1900"]
    plt.plot(global_income, global_life, 'o')
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")

    plt.xscale("log")
    plt.xlim(300, 10000)
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.show()


def main():
    """
1.  Charge la data depuis les paths
2.  Convertie et on affiche
    """
    data_life_expectancy = load("./life_expectancy_years.csv")
    data_income = load(
        "./income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    projection_life(data_income, data_life_expectancy)


if __name__ == "__main__":
    main()
