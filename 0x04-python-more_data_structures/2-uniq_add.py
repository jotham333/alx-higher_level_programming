#!/usr/bin/python3

def uniq_add(my_list=[]):

    uniq = 0
    uniq_num = set(my_list)
    for num in uniq_num:
        uniq += num

    return uniq
