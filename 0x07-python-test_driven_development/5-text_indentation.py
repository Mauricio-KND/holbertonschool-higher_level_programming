#!/usr/bin/python3
"""
Module for text_indentation() function.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :.
    Args:
        text: String of characters.
    Raises:
        TypeError: If argument is not a string of characters.

    Returns:
        Nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in ".?:":
        text = text.replace(c, c + "\n\n")
    print('\n'.join(t.strip() for t in text.split('\n')), end='')
