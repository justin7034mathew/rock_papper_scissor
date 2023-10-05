import random

user_points = 0
computer_points = 0

options = ["rock","papper","scissor"]

while True:
    user_input = input("Type Rock/Papper/Scissor or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue
    random_number = random.randint(0, 2)

    computer_picker = options[random_number]
    print("Computer picked",computer_picker,".")

    if user_input == "rock" and computer_picker == "Scissor":
        print("you won..🥳")
        user_points += 1
    elif user_input == "papper" and computer_picker == "rock":
        print("you won..🥳")
        user_points +1
    elif user_input == "scissor" and computer_picker == "papper":
        print("you won..🥳")
        user_points +=1
    else:
        print("You Lost..😪")
        computer_points += 1

print("You won by",user_points, "points")
print("The computer won by",computer_points,"points")