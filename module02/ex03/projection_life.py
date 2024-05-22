from load_csv import load
import matplotlib.pyplot as plt

def projection_life():

    """
        On load la data depuis les fichier csv

        On extrait les donner avec data_income["1900"] avec une date precise
        
        On charge les donner dans un plot sous format 'o' pour avoir des points 

        On nomme les label et le titre

        On scale l'axe x et on applique un courbe logarithmique pour correspondre au sujet
    """
    data_life_expectancy = load("./life_expectancy_years.csv")
    data_income = load("./income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    
    global_income = data_income["1900"]
    global_life = data_life_expectancy["1900"]
    
    plt.plot(global_income,global_life,'o')
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")

    plt.xscale("log")
    plt.xlim(300, 10000)
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.show()


if __name__ == "__main__":
    main()