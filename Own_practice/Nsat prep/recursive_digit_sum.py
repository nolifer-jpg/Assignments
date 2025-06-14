def recursive_digit_sum(n):
    if n <10:
        return n
    return recursive_digit_sum(n%10 + recursive_digit_sum(n//10))
print(recursive_digit_sum(12345))