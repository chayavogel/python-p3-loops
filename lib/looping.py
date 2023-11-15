#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -=1
    if i == 0:
        print("Happy New Year!")


def square_integers(int_list):
    squared_integers = []
    for integer in int_list:
        squared_integer = integer * integer
        squared_integers.append(squared_integer)
    return squared_integers

def fizzbuzz():
    i = 1
    while i < 101:
        if (i% 3 == 0) and (i% 5 == 0):
            print("FizzBuzz")
        elif (i% 3 == 0):
            print("Fizz")
        elif (i% 5 == 0):
            print("Buzz")
        else:
            print(i)
        i += 1

fizzbuzz()
