import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from load_csv import load


def convert_vals(val: str):
    val_int = val.replace({"K":"*1e3", "M":"*1e6", "B":"*1e9"}, regex=True)\
        .map(pd.eval).astype(int)
    return(val_int)

def main():
    try:
        data = load("population_total.csv")
        if data is None or not isinstance(data, pd.DataFrame):
            raise AssertionError("Could not load data from file")
        spain_data = data.loc["Spain"]
        france_data = data.loc["France"]
        spain_data.index = convert_vals(spain_data.index)
        france_data.index = convert_vals(france_data.index)
    except AssertionError as e:
        print("AssertionError:", e)
    except KeyError as e:
        print("KeyError:", e)
    except TypeError as e:
        print("TypeError:", e)
    except ValueError as e:
        print("ValueError:", e)

    else:
        # 3. Plotting setup
        spain_data.plot()
        france_data.plot()
        # 4. Set exact X-axis range and steps (1800 to 2080 in steps of 40)
        # Note: stop=2081 ensures 2080 is included in the labels
        plt.xlim(1780, 2060)
        plt.xticks(np.arange(1800, 2041, 40))

        # 5. Set exact Y-axis range and steps (30 to 90 in steps of 10)
        # Note: stop=91 ensures 90 is included in the labels
        plt.ylim(0, 80000000)
        plt.yticks(np.arange(0, 81000000, 20000000))

        # 6. Labels and display
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.show()


if __name__ == "__main__":
    main()
