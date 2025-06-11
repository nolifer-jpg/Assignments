def sum_max_min(s):
    s= s.split(" ")
    b = list(map(int, s))
    maximum = max(b)
    minimum = min(b)
    return maximum+minimum
   


print(sum("4 5 1 9 -3 7"))