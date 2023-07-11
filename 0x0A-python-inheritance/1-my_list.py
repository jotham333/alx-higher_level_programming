#!/usr/bin/python3

class MyList(list):
    """Mylist class"""

    def print_sorted(self):
        sorted_lists = sorted(self)
        print(sorted_lists)
