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

from pydoc import plain

"""
# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


# greet_with("Daniel", "Nowhere")
greet_with(location="Nowhere", name="Daniel")"""
"""
#Day8.1 Area calculator
import math
def paint_calc(height, width, cover):
    area=height*width
    num_of_cans=math.ceil(area/cover)

    print(f"You will need {num_of_cans} cans of paint.")

test_h=int(input("Height of wall: "))
test_w=int(input("Width of wall: "))
coverage=5

paint_calc(height= test_h, width=test_w, cover=coverage)"""


# Day 8.2
def prime_checker(number):
    """
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
    """
    """is_prime=True
    for i in range(2, number):
        if number%i==0:
            is_prime=False
    if is_prime:
            print("It's a prime number.")
    else:
        print("It's not a prime number.")


n=int(input("Check this number: "))
prime_checker(number=n)"""


# Day8_Project_Caesar-cipher
from art import logo

print(logo)

alphabet = [
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
]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            # 5*-1=-5
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is: {end_text}")


should_end = True
while should_end:
    direction = input("Type'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = False
        print("Goodbye!")


"""
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]

    print(f"The decoded text is: {plain_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)"""
