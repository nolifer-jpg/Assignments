while True:
    n = int(input("Height (1–8): "))
    if 1 <= n <= 8:
        break

for i in range(1, n+1):
    print(" "*(n-i), end="")  #left spaces  
    print("#"*i, end="")      #left #'s
    print("  ", end="")       #gap
    print("#"*i)              #right #'s
    


