#!/usr/bin/python3

def print_list_integer(my_list=[]):

    """
    print_list_intger : print the content of a list

    Args:
        my_list: the list
    """

    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
