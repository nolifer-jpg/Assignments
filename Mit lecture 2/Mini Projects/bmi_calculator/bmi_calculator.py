name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / height**2
if bmi < 18.5:
    status = "underweight"
elif 18.5 <= bmi < 25:
    status = "normal weight"
elif 25 <= bmi < 30:
    status = "overweight"
else:
    status = "obese"
print(f"{name}, your BMI is {bmi:.2f} and you are classified as {status}.")                        