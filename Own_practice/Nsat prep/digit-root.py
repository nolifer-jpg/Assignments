def digit_root(n):
    
    while len(str(n)) > 1:
        sum  = 0
        for num in str(n):
            sum += int(num)
        n = sum
    return n    
print(digit_root(12345))