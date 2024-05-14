import sys

# Fonction pour compter les caractères de ponctuation dans la chaîne


def find_nb_punctuation(string):
    """
        search all puntuation in a string
    """
    nb_punctuation = 0
    for char in string:
        if char in "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
            nb_punctuation += 1
    return nb_punctuation


def building(string):
    """
        searching for lower case , uppercase,
        punctuation via find_nb_punctuation function , spaces and digits
    """
    number_characters = len(string)
    print("The text contains", number_characters, "characters:")
    lowercases = sum(1 for c in string if c.islower())
    uppercases = sum(1 for c in string if c.isupper())
    punctuations = find_nb_punctuation(string)
    spaces = sum(1 for c in string if c.isspace())
    digits = sum(1 for c in string if c.isdigit())
    print(lowercases, " lower letters\n", uppercases,
          "upper letters\n", punctuations,
          "punctuation marks\n", spaces,
          "spaces\n", digits, "digits\n", )


def main():
    """
        String argument and displays the sums of
        its upper-case characters, lower-case characters,
        punctuation characters, digits and spaces.

        Looking for Error like wrong number of argument

        Get input if no parrams is given
    """
    if len(sys.argv) == 1:
        user_input = input()
        building(user_input)
    else:
        try:
            assert len(sys.argv) == 2, "Wrong number of arguments"
            building(sys.argv[1])
        except AssertionError as msg:
            print("AssertionError:", msg)


if __name__ == "__main__":
    main()
