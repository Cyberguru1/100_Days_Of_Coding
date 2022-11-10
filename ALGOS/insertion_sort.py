#!/usr/bin/python3
import random
"""
Implementation of insertion sort in python
written by hamza
"""

def insertion_sort(array):
    size = len(array)
    i = 1
    while i < size:
        x = array[i]
        j = i - 1
        while j >= 0 and array[j] > x: # check if previous element is greater than x
            array[j+1] = array[j] # go forward to position x and assign bigger element
            j -= 1
        j = j + 1
        array[j] = x
        i += 1


arrays = [random.randrange(0,9) for i in range(15)]
print('unsorted array =',arrays)
insertion_sort(arrays)
print('\nsorted with insertion sort = ',arrays)