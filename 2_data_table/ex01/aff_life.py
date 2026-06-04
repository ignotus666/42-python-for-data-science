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
        if country_data.index is not isinstance(country_data.index, int):
            raise ValueError("Index not an int value")
        # 3. Plotting setup
        country_data.plot()
    except AssertionError as e:
        print("AssertionError:", e)
    except KeyError as e:
        print("KeyError:", e)
    except TypeError as e:
        print("TypeError:", e)
    except ValueError as e:
        print("ValueError:", e)

    # 4. Set exact X-axis range and steps (1800 to 2080 in steps of 40)
    # Note: stop=2081 ensures 2080 is included in the labels
    plt.xlim(1780, 2120)
    plt.xticks(np.arange(1800, 2081, 40))

    # 5. Set exact Y-axis range and steps (30 to 90 in steps of 10)
    # Note: stop=91 ensures 90 is included in the labels
    plt.ylim(25, 95)
    plt.yticks(np.arange(30, 91, 10))

    # 6. Labels and display
    plt.title("Spain Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
