import sys


def convert_to_morse(text):
    """
    Converts a string to morse code, taking a string as a parameter.
    Checks if it's actually a str, and then if it contains valid chars
    (must be a key in the dictionary).
    """

    NESTED_MORSE = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.', ' ': '/',
        }

    assert isinstance(text, str), "the arguments are bad"
    for char in text:
        assert char.upper() in NESTED_MORSE, "the arguments are bad"

    morse_list = []
    for char in text:
        morse_list.append(NESTED_MORSE[char.upper()])
    return ' '.join(morse_list)


def main():
    """
    Main function. Checks if a single argument has been provided,
    and if it has, calls convert_to_morse() to attempt to convert it
    to morse code.
    """

    try:
        assert len(sys.argv) == 2, "the arguments are bad"

        text = sys.argv[1]
        morse_code = convert_to_morse(text)
        print(morse_code)

    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
