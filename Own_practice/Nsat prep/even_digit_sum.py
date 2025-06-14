def even_digit_sum(n):
    sum = 0
    if len(str(n)) %2==0:
        for num in str(n):
            sum += int(num)
        return sum
    else:
        return -1
print(even_digit_sum(123))