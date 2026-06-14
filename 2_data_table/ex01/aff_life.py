import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Loads a .csv file with the load function and checks if it
    has content. Turns the row corresponding to the desired country
    into a pandas series, turns the index year strings into ints.
    Then it plots the data in a matplotlib chart.
    """
    try:
        dataF = load("life_expectancy_years.csv")
        if dataF is None:
            raise AssertionError("Could not load data from file")
        country_data = dataF.loc["Spain"]
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
        plt.xticks(range(1800, 2081, 40))
        plt.ylim(25, 95)
        plt.yticks(range(30, 91, 10))

        plt.title("Spain Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()


if __name__ == "__main__":
    main()
