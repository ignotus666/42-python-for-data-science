import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    try:
        if not os.path.exists(path):
            raise AssertionError("File not found")
        if not path.lower().endswith('.csv'):
            raise AssertionError("Not a .csv file")
        data = pd.read_csv(path, index_col="country")
        return(data)
    
    except AssertionError as e:
        print("AssertionError:", e)
        return None
    