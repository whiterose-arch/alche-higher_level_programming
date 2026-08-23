#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for value in set(my_list):
        total += value
    return total
