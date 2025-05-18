p = input("Enter something: ").lower().replace(" ","")
rev_str = p[::-1]
if rev_str == p:
    print("palindrome")
else:
    print("not a palindrome")    

