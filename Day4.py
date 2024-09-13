import random
from typing import List, Any

"""
import My_module

random_integer = random.randint(1, 10)

print(random_integer)

print(My_module.pi)"""

"""
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score} ")"""
"""
# Day4.1

random_integer = random.randint(0, 1)
if random_integer == 0:
    print("Tails")
else:
    print("Heads")"""

# Day_4.2_List
"""
states_of_america = ["Delaware", "Pensilvanya", "New Jersey", "Georgia"]
print(states_of_america[2])"""

# Challange
"""
names_string = input("Give me everybody's names, separated by a coma: ")
names = names_string.split(", ")
names_inter = len(names)
random_name = random.randint(0, names_inter - 1)
person_who_will_pay = names[random_name]
print(person_who_will_pay + " is going to buy the meal today.")"""

# Day_4.3_Tresure_map
"""
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]


print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you whant to put the tresure? ")

horizontal = int(position[0])  # 2
vertical = int(position[1])  # 3

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")"""

# Day_4_Rock_Paper_Scissors

import random

ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
PAPER = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [ROCK, PAPER, SCISSORS]

# Get the user's choice
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n")
)

# Check if the user choice is valid
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    # Display the user's choice
    print(game_images[user_choice])

    # Generate the computer's choice
    computer_choice = random.randint(0, 2)

    # Display the computer's choice
    print("Computer chose:")
    print(game_images[computer_choice])

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw")
    elif (
        (user_choice == 0 and computer_choice == 2)
        or (user_choice == 1 and computer_choice == 0)
        or (user_choice == 2 and computer_choice == 1)
    ):
        print("You win!")
    else:
        print("You lose!")

"""
map = [ROCK, PAPER, SCISSORS]
map_integer = len(maps)
random_choice = random.randint(0, map_integer - 1)
maps = map.split(", ")
what_computer_chose = names[random_choice]
print(what_computer_chose)

random_choice = random.randint(0, 2)

if random_choice == 0:
    print(ROCK)
elif random_choice == 1:
    print(PAPER)
else:
    print(SCISSORS)
"""
