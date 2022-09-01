#summing from the beginning of the list
def method1(values):
    if len(values)== 0:
        return 0
    return values[0] + method1(values[1:])

#summing from the end of the list

def method2(values):
    if len(values) == 0:
        return 0
    return method2(values[0:len(values)-1]) + values[len(values)-1]

#decomposing the list to single variables and then summing

def method3(values):
    if len(values) == 0 :
        return 0
    if len(values) == 1:
        return values[0]
    return method3(values[0:len(values)//2]) + method3(values[len(values)//2 : len(values)])


#implementing above methods using pointers(lower, upper)

#lower keeps increasing till it reaches or passes upper

def method1_v2(values, lower, upper):
    if lower > upper:
        return 0
    return values[lower] + method1_v2(values, lower+1, upper)


def method2_v2(values, lower, upper):
    if upper < lower:
        return 0
    return values[upper] + method2_v2(values, lower, upper - 1)

list = [1,2,3,4]
print(method1(list))
print(method2(list))
print(method3(list))
print(method1_v2(list, 0, len(list)-1))
print(method2_v2(list, 0, len(list)-1))