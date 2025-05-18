def main():
    t = int(input("Enter the number: "))
    result = is_prime(t)
    if result:
        print(f"{t} is a prime number")
    else:
        print(f"{t} is not a prime number")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

main()