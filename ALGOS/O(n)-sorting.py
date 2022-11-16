#!/usr/bin/env python3

def bubble_sort(array):
    size = len(array)
    sort_flag = False
    i = 0
    while not sort_flag: 
        sort_flag = True
        if i - 1 == size:
            i = 0
        if array[i -1] > array[i]:
            array[i-1], array[i] = array[i], array[i-1]
            sort_flag = False
        i += 1
    print(array)

bubble_sort([3,5,3,2,4,5])