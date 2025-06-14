def digit_root(n):
    new_n = n
    while len(str(new_n))> 1:
        remainder = n % 10
        dividend = n//10
        new_n = remainder+dividend
    return new_n

print(digit_root(38))