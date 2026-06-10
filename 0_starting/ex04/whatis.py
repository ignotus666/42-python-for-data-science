import sys


try:
    if len(sys.argv) < 2:
        sys.exit(0)  # Exit silently if no argument
    elif len(sys.argv) > 2:
        assert False, "AssertionError: more than one argument is provided"
    try:
        val = int(sys.argv[1])
        if val % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        assert False, "AssertionError: argument is not an integer"
except AssertionError as e:
    print(e)
