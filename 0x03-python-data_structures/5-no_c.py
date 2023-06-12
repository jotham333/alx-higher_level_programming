#!/usr/bin/python3

def no_c(my_string):

    """
        no_c: remove character c from string

        Args:
            my_string: the string literal
        
        Returns:the new string

    """

    for i in my_string:
        if i == 'c' or i == 'C':
            index = my_string.index(i)
            new_string = my_string[:index] + my_string[index+1:]
            return new_string
        
    return my_string
