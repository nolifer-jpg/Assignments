def mirror_index(lst):
    for i in range(len(lst)):
        if i == lst[i]:
            return i
    return -1   

print(mirror_index([5, 6, 7]))        