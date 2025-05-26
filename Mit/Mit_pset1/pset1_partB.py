
#inputs from the user 
annual_salary =float(input("Enter your annual salary: ").strip())
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ").strip())
total_cost =float(input("Enter the cost of your dream house: ").strip())
semi_annual_raise = float(input("Enter semi-annual salary raise: "))


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
    if months_required%6 == 0:
        salary_each_month += salary_each_month*semi_annual_raise

#prints the months required
print(f"Months required: {months_required}")