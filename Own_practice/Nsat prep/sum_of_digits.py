def main():
    t = int(input())
    for _ in range(t):
        n = input()
        print(sum_digits(n))


def sum_digits(n):
    sumation =0
    for digit in n:
        sumation += int(digit)
    return sumation    


main()        