##runtime is O(N^2)
##space complexity is O(N)
def select_sort(a):
    if len(a) <= 1:
        return list(a)
    b = list(a)
    min_index = b.index(min(b))
    aux = b[min_index]
    b[min_index] = b[0]
    b[0] = aux
    return [aux] + select_sort(b[1:])

print(select_sort([1,7,4,6,8,6,7]))