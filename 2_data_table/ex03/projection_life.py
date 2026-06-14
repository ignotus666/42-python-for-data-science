import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Loads two .csv files, checks they are the same length and
    that the countries they list are equal in number and position.
    Converts the 1900 column in each to a numpy array and uses those
    to display a scatter plot.
    """
    try:
        life_df = load("life_expectancy_years.csv")
        income_df = load("income_per_person_gdppercapita_"
                         "ppp_inflation_adjusted.csv")
        if life_df is None or income_df is None:
            raise AssertionError("Could not load data from file(s)")
        if len(life_df) != len(income_df):
            raise AssertionError("Dataframe lengths do not match")
        if not life_df["country"].equals(income_df["country"]):
            raise AssertionError("Country lists do not match or "
                                 "are out of order")

        life_exp_data = life_df["1900"].to_numpy()
        gdp_data = income_df["1900"].to_numpy()
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
        x = gdp_data
        y = life_exp_data
        plt.scatter(x, y)

        plt.xscale("log")
        plt.xlim(300, 11000)
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])

        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.show()


if __name__ == "__main__":
    main()
