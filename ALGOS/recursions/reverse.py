##reverse a string with recurrsion time complexity 0(n)
from typing import Any
from sympy import re


def reverse_func(str) -> None:
    length = len(str)

    if length == 1:
        return str[0]

    return str[length-1] + reverse_func(str[0:length-1])

def reverse_func2(str) -> None:
    if str == '':
        return ''
    return reverse_func2(str[1:]) + str[0]

print(reverse_func("hamza"))
print(reverse_func2("gnirtSdesreveR"))