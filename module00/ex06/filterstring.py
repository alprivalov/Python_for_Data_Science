from ft_filter import ft_filter
import sys

def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert len(sys.argv[2]) > 0 and len(sys.argv[1]) > 0, "the arguments are bad"
        assert sys.argv[2].lstrip('-').lstrip('+').isdigit() == True,"argument is not an integer"
        size = int(sys.argv[2])
        split = str.split(sys.argv[1],' ')
        # print(ft_filter.__doc__)
        test = ft_filter(lambda x: len(x) > size,split)
        print([c for c in test])

    except AssertionError as msg:
        print("AssertionError:", msg)


if __name__ == "__main__":
    main()
