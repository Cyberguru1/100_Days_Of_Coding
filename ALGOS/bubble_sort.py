#!/usr/bin/env python3
import random

"""
implementation of bubble sort
"""

def bubble_sort(array):
    size = len(array)
    sort_flag = False
    while not sort_flag: 
        sort_flag = True       
        for i in range(1, size):
            if array[i -1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                sort_flag = False


array = [random.randrange(0,9) for i in range(25)]
print(array)
bubble_sort(array)
print(array)

# ┌──(cyberguru㉿cyberguru)-[~/Documents/alx/100_Days_Of_Coding/ALGOS]
# └─$ time ./bubble_sort.py
# [7, 5, 5, 8, 3, 5, 2, 5, 6, 3, 0, 6, 3, 0, 1, 4, 2, 3, 5, 1, 8, 3, 8, 7, 6]
# [0, 0, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8]

# real    0.09s
# user    0.07s
# sys     0.02s
# cpu     96%