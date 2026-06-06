import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from load_csv import load


def convert_vals(val: str):
    if val.endswith("k"):
        return float(val[:-1]) * 1e3
    elif val.endswith("M"):
        return float(val[:-1]) * 1e6
    elif val.endswith("B"):
        return float(val[:-1]) * 1e9
    else:
        return float(val)

def main():
    try:
        data = load("population_total.csv")
        if data is None or not isinstance(data, pd.DataFrame):
            raise AssertionError("Could not load data from file")
        spain_data = data.loc["Spain"]
        france_data = data.loc["France"]
        spain_data.index = spain_data.index.astype(int)
        france_data.index = france_data.index.astype(int)
        spain_data = spain_data.loc[:2050].map(convert_vals)
        france_data = france_data.loc[:2050].map(convert_vals)
        max_pop = max(max(spain_data), max(france_data))
    except AssertionError as e:
        print("AssertionError:", e)
    except KeyError as e:
        print("KeyError:", e)
    except TypeError as e:
        print("TypeError:", e)
    except ValueError as e:
        print("ValueError:", e)

    else:
        spain_data.plot(label="Spain")
        france_data.plot(label="France")
        
        plt.xlim(1790, 2060)
        plt.xticks(range(1800, 2051, 40))
        
        plt.ylim(0, max_pop + 10000000)
        plt.yticks(range(1, 81000000, 20000000))

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend(loc="lower right")
        plt.show()


if __name__ == "__main__":
    main()
