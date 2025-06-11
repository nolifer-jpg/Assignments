def second_largest(arr):
    if len(set(arr)) == 1:
     return -1
    first = arr[0]
    second = float('-inf')
    for i in range(len(arr)):
        if arr[i]>first:
            second = first
            first = arr[i]
        elif arr[i] < first and arr[i] > second:
           second = arr[i]    
    return second

print(second_largest([7, 5, 7, 3]))