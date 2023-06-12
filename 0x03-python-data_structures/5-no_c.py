#!/usr/bin/python3

def no_c(my_string):

    """
        no_c: remove character c from string

        Args:
            my_string: the string literal
        
        Returns:the new string

    """

    new_string = my_string.translate({ord(i): None for i in 'cC'}) 
    return new_string
