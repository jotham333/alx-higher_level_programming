#!/usr/bin/python3

def element_at(my_list, idx):

    """
    element_at: retrieve the element at a
    specific index in the list

    Args:
        my_list: the list
        idx: the index

    Returns:
        The element at the given index, or None if the
        index is out of range
    """
    list_len = len(my_list)

    if idx >= list_len or idx < 0:
            return (None)

    return (my_list[idx])
