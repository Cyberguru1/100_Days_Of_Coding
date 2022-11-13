#!/usr/bin/env python3

def printArray(array:[int]) -> int:
    """
    prints the array
    """
    print(array[1:])

def reverseArray(array:[int]) -> int:

    j = array[0] + 1
    i = 1
    while i < j:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        i += 1
        j -= 1
    printArray(array)

def sortArray(array:[int]) -> int:
    ##solution one 1
    def sort_min(array):
        arrlen = len(array)
        i = 1
        while i < arrlen:
            jj = i - 1
            x = array[i]
            while jj >= 0 and array[jj] > x:
                array[jj + 1] = array[jj]
                jj -= 1
            jj += 1
            array[jj] = x
            i += 1

    arrlen = array[0] + 1
    array_odd = []
    array_even = []
    for i in range(1, arrlen):
        if array[i] % 2 == 0:
            array_even.append(array[i])
        else:
            array_odd.append(array[i])
    print(array_even,array_odd)

    sort_min(array_odd)
    sort_min(array_even)
    array = array_odd + array_even
    print(array)

array = [12,1,2,3,4,5,6,3,5,6,4,2,0]

sortArray(array)

        
