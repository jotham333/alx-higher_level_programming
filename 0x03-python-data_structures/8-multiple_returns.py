#!/usr/bin/python3

def multiple_returns(sentence):

    """
        multiple: returns multiple variable

        Args:
            sentence: The parameter

        Returns: multiple variable
    """
    str_len = len(sentence)
    first_char = sentence[0]


    if str_len == 0:
        first_char = None
        return first_char

    return str_len, first_char
