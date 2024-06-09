"""
#Data types

#String

print("Hello"[4])

#Integer

print(123+345)
123_456_789

#Float

3.14159

#Boolean

True
False
"""
"""
num_char = len(input("What is your name? "))

print(type(num_char)) #arata tipul variabilei, in acest caz este integer

new_num_char = str(num_char) #transforma integer in string pt a fi citit si concatanat cu string

print("Your name has " + new_num_char + " characters.")#toate datele sa fie afisate trebuie sa fie de acelas fel(string in cazul acesta)
"""
"""
a=float(123)
print(type(a))

print(70 + float("100.5")) #poti converti string in float prin scrierea float in fata

print(str(70)+ str(100))# aici este o concatanare de string si va afisa 70100
"""
"""
two_digit_number=input("Type a two digit number: \n")
print(type(two_digit_number))# va afisa ca sunt string
first_digit=two_digit_number[0]#va lua primul nr din cele doua scrise de mine in imput
second_digit=two_digit_number[1]#va lua a doilea nr din cele doua
print(first_digit)
print(second_digit)
result=int(first_digit) + int(second_digit)# am convertit string in integer pt a face adunarea numerelor, altfel facea o concatenare
print(result)
"""

#Day 2.2 BMI calculator
"""
height=input("enter your height in m: ")
weight=input("enter your height in kg: ")

BMI=int(weight)/float(height)**2

BMI_as_int=int(BMI)
print(BMI_as_int)"""

#day 2 end
"""result=4/2
result/=2
print(result)
score=0
height=1.8
isWinning=True

#f-string
print(f"your score is: {score}, your height is {height}, you are winning is {isWinning}")"""

# Day 2.3 Exercitiu
"""
age=input("What is your curent age? ")
age_as_int=int(age)
a=90-age_as_int
x=365*(a) #zile
y=52*(a) #saptamani
z=12*(a) #luni
message=f"You have {x} days, {y} weeks, and {z} months left"
print(message)"""

# Day 2.Proiect final - calculator de factura si bacsis
print("Welcome to tip calculator!")
cat_este_suma=float(input("What was the total bill? $"))

tips=int(input("What procentage tip would you like to give? 10, 12, or 15? "))

split_bill=int(input("How many people to split the bill? "))

tip_as_percent=tips/100
total_tip_amount=cat_este_suma*tip_as_percent
total_bill=cat_este_suma+total_tip_amount
bill_per_person=total_bill/split_bill

final_amount=round(bill_per_person, 2)
final_amount="{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")