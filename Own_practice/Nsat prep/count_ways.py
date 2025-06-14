def count_ways(n):
    if n == 0:
        return 1
    elif n<0:
        return 0
    else:
        return count_ways(n-1) +count_ways(n-2)

print(count_ways(4))