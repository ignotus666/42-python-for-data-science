import sys
from ft_filter import ft_filter


def main():
    """
    Main function. Checks no. of args and whether they are
    valid types, then splits the string into words and applies
    a lambda to filter out those longer than N, printing them
    as a list.
    """
    try:
        assert len(sys.argv) == 3, "AssertionError"
        S = sys.argv[1]
        N = int(sys.argv[2])
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")
        return

    words = S.split()
    longer_words = ft_filter(lambda w: len(w) > N, words)
    print(longer_words)


if __name__ == "__main__":
    main()