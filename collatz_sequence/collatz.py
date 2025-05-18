def collatz(n, steps=0):
    print(n, end=" → " if n!=1 else "\n")
    if n==1:
        print(f"Total steps: {steps}")
        return steps
    elif n%2==0:
        return collatz(n//2, steps+1)
    else:
        return collatz(3*n+1, steps+1)


number = int(input("Enter a number: "))
collatz(number)