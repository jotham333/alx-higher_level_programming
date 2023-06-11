#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
        replace_in_list: replace an element of a list at a specfic position

        Args:
            my_list: the list

            idx: the index

            element: the element to replace

        Returns: the list

    """

    if idx < 0 or idx  >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
