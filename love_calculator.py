# I developed a fun love calculator the details about how to calculate can be found at https://math.answers.com/other-math/How_do_you_calculate_love_on_paper 
# or simply google how to calculate true love by hand  :)
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1 = name1.lower()
name2 = name2.lower()
name1_t = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
name1_l = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
name2_t = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
name2_l = name2.count("l") + name2.count("o") +name2.count("v") + name2.count("e")
true_score = str(name1_t + name2_t)
love_score = str(name1_l + name2_l)
total_score = int(true_score + love_score)
if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else :
    print(f"Your score is {total_score}.")