'''water_level=50
if water_level>80:
    print("Drain water")
else:
    print("Continue")'''

#conditionali if si else
'''
print("Welcome to the rellercoster!")
height=int(input("What is your height in cm: "))
if height>=120:
    print("You can ride the rollercoster!")
else:
    print("Sorry, you have to grow taller before you can ride.")'''

#Day3.1 Odd or Even
'''
number= int(input("Introdu numarul dorit: "))
if number%2==0:
    print("This is an even number.")
else:
    print("This is an odd number.")'''

#Day-3.1
'''
print("Welcome to the rellercoster!")
height=int(input("What is your height in cm: "))
if height>=120:
    print("You can ride the rollercoster!")
    age=int(input("What is your age? "))
    if age<12:
        print("Please pay 5$")
    elif age<=18:
        print("Please pay 7$")
    else:
        print("Please pay 12$")
else:
    print("Sorry, you have to grow taller before you can ride.")'''

#Day-3.2
'''weight=float(input("What is your weight in Kg: "))
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
    print(f"Your bmi is {bmi}, you are clinically obese!!!!!!")'''

'''
num=int(input('Enter the number: '))
if(num%2==0 and num!=0):
    num=num*2
    print('Double of given number is ',num)
elif(not num%2==0 and num!=0):
    num=num*3
    print('Triple of given number is ',num)
else:
    print('0')'''

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

#Day