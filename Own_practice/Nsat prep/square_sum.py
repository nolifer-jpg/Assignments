def sq_sum(s):
    s = s.split(" ")
    new_s = list(map(int, s))
    sum =0
    for digit in new_s:
        sum += digit**2
    return sum

print(sq_sum("2 3 4"))    