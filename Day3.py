"""water_level=50
if water_level>80:
    print("Drain water")
else:
    print("Continue")"""

# conditionali if si else
"""
print("Welcome to the rellercoster!")
height=int(input("What is your height in cm: "))
if height>=120:
    print("You can ride the rollercoster!")
else:
    print("Sorry, you have to grow taller before you can ride.")"""

# Day3.1 Odd or Even
"""
number= int(input("Introdu numarul dorit: "))
if number%2==0:
    print("This is an even number.")
else:
    print("This is an odd number.")"""

# Day-3.1
"""
print("Welcome to the rellercoster!")
height=int(input("What is your height in cm: "))
bill=0

if height>=120:
    print("You can ride the rollercoster!")
    age=int(input("What is your age? "))
    if age<12:
        bill=5
        print("Child tikets are 5$")
    elif age<=18:
        bill=7
        print("Youth tikets are 7$")
    else:
        bill=12
        print("Adult tikets are 12$")
    wants_photo=input("Do you want a photo taken? y or n.")
    if wants_photo=="y":
        bill+=3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
"""
# Day-3.2
"""weight=float(input("What is your weight in Kg: "))
height=float(input("What is your height in m: "))

bmi=round(weight/height**2)

if bmi<18.5:
    print(f"Your bmi is {bmi}, you are underweight!")
elif bmi<=25:
        print(f"Your bmi is {bmi}, you have a normal weight!")
elif bmi<=30:
        print(f"Your bmi is {bmi}, you are overweight!")
elif bmi<=35:
        print(f"Your bmi is {bmi}, you are obese!")
else:
    print(f"Your bmi is {bmi}, you are clinically obese!!!!!!")"""

"""
num=int(input('Enter the number: '))
if(num%2==0 and num!=0):
    num=num*2
    print('Double of given number is ',num)
elif(not num%2==0 and num!=0):
    num=num*3
    print('Triple of given number is ',num)
else:
    print('0')"""
"""
#Day3.3 Leap Year Exercise

year=int(input("Which year do you want to check? "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap year!")
        else:
            print("No Leap year!")
    else:
        print("Leap year!")
else:
    print("No Leap year!")
"""
# Day 3.4 Exercise
"""
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? y or n: ")
extra_cheese = input("Do you want extra cheese? y or n: ")
bill = 0
if size == "S":
    bill += 15

elif size == "M":
    bill += 20

else:
    bill += 25
if add_pepperoni == "y":
    if size == "S":
        bill += 2
    else:
        bill += 3


if extra_cheese == "y":
    bill += 1

print(f"Your final bill is ${bill}")
"""
# Day 3.4.1
"""
print("Welcome to the rellercoster!")
height = int(input("What is your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tikets are 5$")
    elif age <= 18:
        bill = 7
        print("Youth tikets are 7$")

    elif age >= 45 and age <= 55:
        print("You have free ride! ")

    else:
        bill = 12
        print("Adult tikets are 12$")

    wants_photo = input("Do you want a photo taken? y or n.")
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
"""
# 3.5 Love calculator
"""
print("Welcome to Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))


if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos!")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}")"""

# Day 3.Final
print("Welcome to tresure island!")

cross_roads = input(
    "You are at a cross roads where do you chose to go left or right? Type L for left or R for right.\n"
).lower()


if cross_roads == "l":

    swim_or_wait = input(
        "You reach at a lake. What will you do? Type W for wait or S for swim.\n"
    ).lower()

    if swim_or_wait == "w":

        doors = input(
            "You reach in front of 3 doors, red, blue, yellow. Type R for red, B for blue or Y for yellow.\n"
        ).lower()

        if doors == "y":
            print("You win the game!")
        elif doors == "r":
            print("You are on fire. Game over!")
        elif doors == "b":
            print("You freezed. Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")
