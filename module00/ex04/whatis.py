import sys


def whatis():
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) > 1:
            arg_is_digit = sys.argv[1].lstrip('-').lstrip('+').isdigit()
            assert arg_is_digit, "argument is not an integer"
            number = int(sys.argv[1])
            if number % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
    except AssertionError as msg:
        print("AssertionError:", msg)


def main():
    whatis()


if __name__ == "__main__":
    main()
