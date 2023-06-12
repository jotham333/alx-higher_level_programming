#!/usr/bin/python3

def multiple_returns(sentence):

    """
        multiple: returns multiple variable

        Args:
            sentence: The parameter

        Returns: multiple variable
    """

    if len(sentence) == 0:
        return None

    str_len = len(sentence)
    first_char = sentence[0]

    return str_len, first_char
