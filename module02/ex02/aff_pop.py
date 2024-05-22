import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def clean_value(value):
    """
        def clean_value(value):  prend une liste flatte en params

        Fonction pour supprimer les suffixes "M" et "K" et convertir en nombre
        
        return float(value[:-1]) * 1e6  # return un nombre convertir en millions
        
        return float(value[:-1]) * 1e3  # return un nombre convertir en milliers
    
    """
    if value.endswith('M'):
        return float(value[:-1]) * 1e6 
    elif value.endswith('K'):
        return float(value[:-1]) * 1e3
    else:
        return float(value)

def aff_pop(data : pd.DataFrame):
    france = data[data["country"] == "France"]
    Belgium = data[data["country"] == "Belgium"]

    plt.xlabel("Year")
    plt.ylabel("Life expectancy")

    bl_data = [clean_value(value) for value in Belgium.values.flatten().tolist()[1:]]
    fr_data = [clean_value(value) for value in france.values.flatten().tolist()[1:]]
    years = france.columns[1:].values.astype(int)
    plt.plot( years, bl_data,"b", label="Belgium")
    plt.plot( years, fr_data,"g", label="France")

    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2040)

    max_pop = max(max(bl_data), max(fr_data))
    print(max_pop)
    
    y_ticks = [i *1e7  for i in range(2,int(max_pop/1e7) + 1,2)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])

    plt.legend()
    plt.show()