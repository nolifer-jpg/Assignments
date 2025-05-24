
#inputs from the user 
annual_salary =float(input("Enter your annual salary: ").strip())
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ").strip())
total_cost =float(input("Enter the cost of your dream house: ").strip())



#the variables required for the calculation
salary_each_month = annual_salary/12 
portion_down_payment = 0.25
current_savings = 0
r = 0.04
annual_r = r/12
months_required = 0
down_payment = portion_down_payment*total_cost

#the loop for calculation months
while current_savings < down_payment:
    current_savings += portion_saved*salary_each_month+current_savings*annual_r
    months_required += 1

#prints the months required
print(f"Months required: {months_required}")