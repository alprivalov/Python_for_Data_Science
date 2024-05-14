import pandas as ps

def load(path: str) -> ps.DataFrame:
    test = ps.read_csv(path)
    print("Loading dataset of dimensions",test.shape)
    return test