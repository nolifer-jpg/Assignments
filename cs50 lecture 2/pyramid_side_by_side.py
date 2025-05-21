n = int(input("Enter the height of the pyramid: "))
for i in range(1, n+1):
    print(" "*(n-i), end="")  #left spaces  
    print("#"*i, end="")      #left #'s
    print("  ", end="")       #2 spaces
    print("#"*i)              #right #'s


