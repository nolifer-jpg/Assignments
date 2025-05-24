num = int(input("How many numbers? "))#number of input user wants to give

#varibles required
even = 0
odd = 0


#even/odd checking function
def is_even(n):
   return n%2 == 0

#loop for repeating untill user inputed value is satisfied
for i in range(num):
    x = int(input("Enter a number: "))
    if is_even(x):
        even += 1
    else:
        odd +=1

#print the number if times the user has inputed even and odd
print(f"Even: {even}")
print(f"Odd: {odd}")





