import matplotlib.pyplot as plt
from load_csv import load


def convert_vals(val: str) -> int:
    """
    Converts suffixed values into ints so they can
    be used in the main function.
    """
    if val.endswith("k"):
        return int(float(val[:-1]) * 1e3)
    elif val.endswith("M"):
        return int(float(val[:-1]) * 1e6)
    elif val.endswith("B"):
        return int(float(val[:-1]) * 1e9)
    else:
        return int(float(val))


def main():
    """
    Loads a .csv file with the load function and checks if it
    has content. Turns the rows corresponding to the desired countries
    into pandas series, turns the index year strings into ints.
    Limits the data untl the year 2050 and uses the convert_vals function
    to convert the k, M and B suffixes into usable ints. Determines max
    population values to determine range on y axis. Converts ints back into
    suffixed values for the y axis.
    Then it plots the data in a matplotlib chart.
    """
    try:
        dataF = load("population_total.csv")
        if dataF is None:
            raise AssertionError("Could not load data from file")
        spain_data = dataF.loc["Spain"]
        france_data = dataF.loc["France"]
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
    except Exception as e:
        print("Exception:", e)

    else:
        spain_data.plot(label="Spain")
        france_data.plot(label="France")

        plt.xlim(1790, 2060)
        plt.xticks(range(1800, 2051, 40))

        plt.ylim(0, max_pop + 2000000)
        y_ticks = list(range(0, max_pop + 1, 20000000))
        y_labels = []
        for v in y_ticks:
            if v == 0:
                y_labels.append("")
            elif v >= 1e9:
                y_labels.append(f"{int(v / 1e9)}B")
            elif v >= 1e6:
                y_labels.append(f"{int(v / 1e6)}M")
            elif v >= 1e3:
                y_labels.append(f"{int(v / 1e3)}k")
            else:
                y_labels.append(str(int(v)))
        plt.yticks(y_ticks, y_labels)

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend(loc="lower right")
        plt.show()


if __name__ == "__main__":
    main()
