import sys
import string


def main():
    """
    Counts the number of upper/lower letters,
    punctuation, spaces and digits in a string.
    """
    try:
        if len(sys.argv) < 2:
            user_input = input("What is the text to count?\n")
        elif len(sys.argv) > 2:
            assert False, "AssertionError: just one argument please!"
        else:
            user_input = sys.argv[1]

        upper = 0
        lower = 0
        punct = 0
        digit = 0
        space = 0

        s = user_input
        for char in s:
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
            elif char in string.punctuation:
                punct += 1
            elif char.isdigit():
                digit += 1
            elif char.isspace():
                space += 1

        print(f"The text contains {len(s)} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punct} punctuation marks")
        print(f"{space} spaces")
        print(f"{digit} digits")
    except AssertionError as e:
        print(e)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
