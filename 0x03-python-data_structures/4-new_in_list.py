#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    new_in_list: replaces an element in a list at specific position

    Args:
        my_list: the list

        idx: the position

        element: the element

    Returns: The new_list or original_list if conditions are not met
    """

    new_list = my_list[:]

    if idx < 0 or idx >= len(my_list):
        return my_list

    else:
        new_list[idx] = element
        return new_list
