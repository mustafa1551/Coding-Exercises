#flow chart is included in the repository for the code works and to understand how to calculate a leap year
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
 print("Leap year.")
elif year % 100 == 0:
  if year % 400 == 0:
      print("Leap year.")
else: 
    print("Not leap year.")

