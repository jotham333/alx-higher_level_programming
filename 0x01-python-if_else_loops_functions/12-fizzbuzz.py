#!/usr/bin/python3

"""This print numbers from 1 - 100 separated by space.
    Fizz replaces number that are multiples of three
    Buzz replaces number that are multiples of five
    FizzBuzz replaces numbers that multiple of three and five"""


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        elif number % 3 == 0 and  number % 5 == 0:
            print("FizzBuzz ", end="")
        else: print("{} ".format(number, end="")
