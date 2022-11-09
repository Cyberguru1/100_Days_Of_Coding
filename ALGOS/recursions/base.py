##written by cyberguru1

def decimal_to_base(n:int, b:int) -> int:
    if n < b:
        return n
    return 10 * decimal_to_base(n // b, b) + (n % b)

print(decimal_to_base(142, 5))
print(decimal_to_base(142, 4))
print(decimal_to_base(142, 3))
print(decimal_to_base(142, 2))