from ft_filter import ft_filter
import sys


def main():
    """
a programe take 2 argument 1 string and 1 int
filter all the word in the string with a min len of the int argument
using lambda to filter the split in good size
output de value as an array
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        len_tmp = len(sys.argv[2]) > 0 and len(sys.argv[1]) > 0
        assert len_tmp, "the arguments are bad"
        is_digit = sys.argv[2].lstrip('-').lstrip('+').isdigit()
        assert is_digit, "the arguments are bad"
        size = int(sys.argv[2])
        split = str.split(sys.argv[1], ' ')
        test = ft_filter(lambda x: len(x) > size, split)
        print([c for c in test])

    except AssertionError as msg:
        print("AssertionError:", msg)


if __name__ == "__main__":
    main()
