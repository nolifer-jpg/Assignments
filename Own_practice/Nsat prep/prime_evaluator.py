def prime_evaluator(s):
    n = len(s)
    for i in range(1, n):
        if n %i == 0:
            if s[:i]*(n//i) == s:
                return "NO"
    return "YES"

print(prime_evaluator("abcdacde"))