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
    my_tuple = ()

    if str_len == 0:
        my_tuple = 0, "None"

    else:
        my_tuple = str_len, first_char
        return my_tuple
