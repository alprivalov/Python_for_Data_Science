import sys


def whatis():
    try:
        assert len(sys.argv) <= 2 ,"more than one argument is provided"
        if len(sys.argv) > 1:
            assert sys.argv[1].lstrip('-').lstrip('+').isdigit() == True,"argument is not an integer"
            number = int(sys.argv[1])
            if number % 2 == 0:
                print("I'm Even")
            else:
                print("I'm Odd.")

    except AssertionError as msg:
        print("AssertionError: ",msg)
        

whatis()
