# Takes the starting and ending population 
n= int(input("Enter starting population: "))
n_target = int(input("Enter target population: "))


#function to check how many years it will take to match the target population
def population_check(n, n_target):
    years = 0
    while n< n_target:
        n = n+ (n//3) - (n//4)
        years += 1
    return years    

#prints the year required
print("Years required: ", population_check(n, n_target), sep="")    