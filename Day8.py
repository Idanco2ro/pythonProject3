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


# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


# greet_with("Daniel", "Nowhere")
greet_with(location="Nowhere", name="Daniel")
