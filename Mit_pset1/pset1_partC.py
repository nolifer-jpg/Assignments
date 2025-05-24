#inputs from the user
annual_salary = float(input("Enter annual salary: "))
semi_annual_raise = 0.07
r = 0.04/12
total_cost = 1000000
down_payment = 0.25*total_cost


#variables for calculation
months = 36
epsilion = 100
low = 0 
high = 10000
possible = True
current_savings = 0
starting_salary = annual_salary
steps=0

#checking if possible to save for 36 months
def check_savings(portion_saved):
    salary = starting_salary
    monthly_salary= salary/12
    savings = 0
    for month in range(1,months+1):
        savings += savings*r
        savings += portion_saved*monthly_salary
        if month%6==0:
            salary += salary*semi_annual_raise
            monthly_salary = salary/12
    return savings

#check for 100% portion saved 
if check_savings(1.0)< down_payment:
    print("It is not possible to pay the down payment in three years")
    possible = False

#Bisection search
while possible:
    guess = (low+high)//2
    portion_saved = guess/10000
    current_savings= check_savings(portion_saved)
    steps +=1
    if abs(current_savings-down_payment)<=epsilion:
        break
    elif current_savings<down_payment:
        low = guess
    else:
        high = guess

if possible:
    print(f"Best savings rate: {round(portion_saved, 4)}")     
    print(f"Steps in bisection search: {steps}")   
