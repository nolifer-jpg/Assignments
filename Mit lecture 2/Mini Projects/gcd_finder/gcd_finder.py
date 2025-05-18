a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

while b != 0:
    temp = b
    b = a % b
    a = temp

print("GCD is:", a)
