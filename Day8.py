"""
def greet():
    print("Hello!")
    print("Daniel")
    print("How are you?")


greet()

# Function that allows for input


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print("Hello ")


# {name} is parameter and "Daniel" is argument

greet_with_name("Daniel")"""

'''
# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


# greet_with("Daniel", "Nowhere")
greet_with(location="Nowhere", name="Daniel")'''
'''
#Day8.1 Area calculator
import math
def paint_calc(height, width, cover):
    area=height*width
    num_of_cans=math.ceil(area/cover)

    print(f"You will need {num_of_cans} cans of paint.")

test_h=int(input("Height of wall: "))
test_w=int(input("Width of wall: "))
coverage=5

paint_calc(height= test_h, width=test_w, cover=coverage)'''

#Day 8.2
def prime_checker(number):
    '''
    if number>1:

            # Iterate from 2 to n // 2
        for i in range(2, (number//2)+1):

                # If num is divisible by any number between
                # 2 and n / 2, it is not prime
            if(number%i)==0:
                print(f"{number} is not a prime number")

        else:
            print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
    '''
    is_prime=True
    for i in range(2, number):
        if number%i==0:
            is_prime=False
    if is_prime:
            print("It's a prime number.")
    else:
        print("It's not a prime number.")


n=int(input("Check this number: "))
prime_checker(number=n)