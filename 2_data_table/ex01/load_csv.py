import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    Receives a path string to load a .csv file. Tests if
    the file exists and is of the correct type.
    Converts it into a dataFrame and return that.
    """
    try:
        if not os.path.exists(path):
            raise AssertionError("File not found")
        if not path.lower().endswith('.csv'):
            raise AssertionError("Not a .csv file")
        dataF = pd.read_csv(path, index_col="country")
        print("Loading dataset of dimensions", dataF.shape)
        return (dataF)

    except AssertionError as e:
        print("AssertionError:", e)
        return None
    except Exception as e:
        print("Exception:", e)
        return None
