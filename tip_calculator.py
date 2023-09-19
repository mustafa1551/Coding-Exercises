#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")
original_bill = float(input("What was the total bill? " ))
tip = int(input("What percantage tip would you like to tip 10, 12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))


bill_with_tip = (original_bill/ 100) * tip + original_bill
new_bill_per_person = bill_with_tip / number_of_people
rounded_number = format(new_bill_per_person,".2f")
print(f"Each person should pay " + rounded_number + "$")