import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
computers_choice = random.randint(0,2)
if computers_choice == user_choice:
 print("You have chosen:\n"+choices[user_choice]+"Computer has chosen the same :\n"+choices[computers_choice]+"Its a draw.")
elif computers_choice ==  0 and user_choice ==1:
  print("You have chosen paper:\n"+choices[user_choice]+"Computer has chosen rock \n" +choices[0] +"\nYou've won.")
elif computers_choice ==0 and user_choice == 2:
    print("You have chosen scissors\n"+choices[user_choice]+"Computer has chosen rock \n") + choices[0]+ "\nComputer won."
elif computers_choice == 1 and user_choice == 0:
     print("You have chosen rock:\n"+choices[user_choice]+"Computer has chosen paper \n" + choices[1]+"\n Computer won.")
elif computers_choice == 1 and user_choice ==2:
  print("You have chosen scissors:\n"+choices[user_choice]+"Computer has chosen paper\n" + choices[1]+"\nYou've won.")
elif computers_choice == 2 and user_choice == 0:
  print("You have chosen rock:\n"+choices[user_choice]+"Computer has chosen scissors\n" + choices[2] + "\nYou've won.")
elif computers_choice == 2 and user_choice ==1:
  print("You have chosen paper:\n"+choices[user_choice]+"Computer has chosen scissors\n"+ choices[2]+"\nComputer won.")
