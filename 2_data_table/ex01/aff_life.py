import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from load_csv import load


def main():
    try:
        data = load("life_expectancy_years.csv")
        if data is None or not isinstance(data, pd.DataFrame):
            raise AssertionError("Could not load data from file")
        country_data = data.loc["Spain"]
        country_data.index = country_data.index.astype(int)
    except AssertionError as e:
        print("AssertionError:", e)
    except KeyError as e:
        print("KeyError:", e)
    except TypeError as e:
        print("TypeError:", e)
    except ValueError as e:
        print("ValueError:", e)
    except Exception as e:
        print("Exception:", e)

    else:
        country_data.plot()
        plt.xlim(1780, 2120)
        plt.xticks(np.arange(1800, 2081, 40))
        plt.ylim(25, 95)
        plt.yticks(np.arange(30, 91, 10))

        plt.title("Spain Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()


if __name__ == "__main__":
    main()
