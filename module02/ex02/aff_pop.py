import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def aff_pop(data : pd.DataFrame):
    france = data[data["country"] == "France"]
    Belgium = data[data["country"] == "Belgium"]
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")

    test = france.columns[1:,]
    b =0
    for c,cr in enumerate(test):
        if int(cr) == 2050:
            b = c
    x = france.columns[0:b]
    y = Belgium.iloc[0,0:b]
    # print(france.iloc[0,0:b].iloc[1])
    # x1 = np.linspace(0, len(france.columns[0:b]), b, endpoint=True)
    # x2 = np.linspace(0, len(Belgium.columns[0:b]), b, endpoint=True)
    # Sélectionner les colonnes contenant les valeurs de population pour les deux pays
    plt.plot( x, Belgium.iloc[0,0:b],"b", label="Belgium")
    plt.plot( x, france.iloc[0,0:b],"g", label="France")
    print(Belgium.iloc[0,1:b],france.iloc[0,0:b] )    
    plt.yticks([0,100,200,300,400,600])
    plt.xticks(np.arange(1, len(Belgium.columns[0:b]), step=40))
    plt.legend()
    plt.show()