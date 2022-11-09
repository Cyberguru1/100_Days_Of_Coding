##finding max element in a list using 
#divide and conquer implemented through recursion


def max_element_DaC(values) -> int:

    if len(values) == 1:
        return values[0]
    length = len(values)
    middle = length // 2
    m1 = max_element_DaC(values[0:middle])
    m2 = max_element_DaC(values[middle:length])

    return max(m1, m2)

def max_element_pointer_Dac(values, lower, upper) -> int:

    if lower == upper:
        return values[upper]

    middle = (lower + upper) // 2

    m1 = max_element_pointer_Dac(values, lower, middle)
    m2 = max_element_pointer_Dac(values, middle + 1, upper)

    return max(m1, m2)

list = [1,4,6,7,2,5,2]

#print(max_element_DaC(list))
#print(max_element_pointer_Dac(list, 0, len(list)-1))


def breaklsb(n):

    if n < 10:
        print(n)
    else:
        breaklsb(n // 10)
        print(n % 10)
    
    
    
breaklsb(2743)
breaklsb(12345)
    