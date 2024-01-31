#!/usr/bin/python3
"""module for text_indentation method"""


def text_indentation(text):
    """
    print a text

    Args:
        text: argument of type string

    Raises:
        TypeError: text must be a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for ch in  ".:?":
        text = (ch + '\n\n').join(
            [line.strip(" ") for line in text.split(ch)])
    print(text, end="")

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
