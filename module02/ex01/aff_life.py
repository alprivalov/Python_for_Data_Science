import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def aff_life(data: pd.DataFrame):
    france = data[data["country"] == "France"]
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.plot(france.columns[1:], france.iloc[0:,1:])
    plt.xticks(france.columns[1::40])
    plt.show()