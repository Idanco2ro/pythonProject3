"""
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)
"""

"""
# Day5.1
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
# sum the total height
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

# find number of students
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

# find average heights:
average_height = round(total_height / number_of_students)
print(f"The average height is {average_height} cm")
"""
"""
# Day5.2
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
hieghts_score = 0
for score in student_scores:
    if score > hieghts_score:
        hieghts_score = score
print(f"The highest score in class is: {hieghts_score}")"""
# Day5.2-end
# For Loop with Range
# for number in range(1, 11, 3):
#    print(number)
"""
total = 0
for number in range(1, 101):
    total += number
print(total)"""
"""
# 5.3 Provocare (Challenge)
sum_even = 0
for number in range(2, 101, 2):
    sum_even += number
print(sum_even)

sum_even2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum_even2 += number
print(sum_even2)"""
"""
# 5.4 Challenge - FizzBuzz game
total = 0
for number in range(1, 101):
    total += number
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)"""
"""
# Challenge password generator
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# asked the user for inputs and saved in integer variables
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# create a list with random caracter

# random_caracter = 0
# letter = letters.split(", ")
# letter_inter = len(letter)
# random_caracter += nr_letters"""
"""
password = ""
# nr_letters=4
for letter in range(1, nr_letters + 1):
    # 1 - 4

    password += random.choice(letters)

for letter in range(1, nr_symbols + 1):

    password += random.choice(symbols)

for letter in range(1, nr_numbers + 1):

    password += random.choice(numbers)

print(password)"""
from random import shuffle

"""
# Hard_level
password_list = []
for letter in range(1, nr_letters + 1):
    # 1 - 4

    password_list += random.choice(letters)

for letter in range(1, nr_symbols + 1):

    password_list += random.choice(symbols)

for letter in range(1, nr_numbers + 1):

    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for letter in password_list:

    password += letter

print(f"Your password is: {password}")"""
"""
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")"""
