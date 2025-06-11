def sum_odd(s):
    sum = 0
    for char in s:
        if not int(char)%2==0:
            sum += int(char)
    return sum

print(sum_odd("123456"))          