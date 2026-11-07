import sys
import random
my_first_game = input(
    "\nplease enter a number:\n1 : stone\n2 : paper\n3 : scissors\n\n")

if my_first_game.isdigit():
    your_choice = int(my_first_game)
    if (your_choice > 3 or your_choice < 1):
        print("it's not a valid number")
        sys.exit()
    computer_value = random.choice("123")
    computer_choice = int(computer_value)
    print("your choice is " + my_first_game +
          " \ncomputer choice " + computer_value)
    if your_choice == 1 and computer_choice == 3:
        print("you win!")
    elif your_choice == 2 and computer_choice == 1:
        print("you win!")
    elif your_choice == 3 and computer_choice == 2:
        print("you win!")
    elif your_choice == computer_choice:
        print("tie game")
    else:
        print("computer win")
else:
    print("you must enter a valid number.")
