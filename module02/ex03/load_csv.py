import pandas as ps

def load(path: str) -> ps.DataFrame:
    """
        On read le path pour recuperer les donnee depuis un .csv
    """
    test = ps.read_csv(path)
    print("Loading dataset of dimensions",test.shape)
    return test