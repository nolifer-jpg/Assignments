height = int(input("What should be the height of the triangle: "))
for i in range(height):  #loops from 0 to height-1 
    j=height-1          #set j for the inner loop
    while True:         #infinite loop until desired value is found
        if j>i:         #for printing the spaces 
            print(" ", end="") #print the spaces without going to the next line in the end
        else:           #for printing the #
            print("#"*(i+1))
            break       #exit the infinite loop
        j-=1
