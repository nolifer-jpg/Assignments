def second_largest(lst, n):
    first = lst[0]
    second = 0
    i =0
    while i != n:
        if lst[i]>first:
            second = first
            first = lst[i]
        elif lst[i]>second and lst[i] != first:
            second = lst[i]
        i +=1
    return second
print(second_largest([1,2,3,4], 4))
