
def reverse_func(str) -> None:
    if len(str) == 1:
        return str[0]
    return str[len(str)-1] + reverse_func(str[0:len(str)-1])

print(reverse_func("hamza"))