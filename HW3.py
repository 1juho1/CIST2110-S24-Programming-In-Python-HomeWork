# HW3.py
# Author: Justin Hoang

# This Homework assignment is meant to test your ability to make functions within python as well as importing and using modules. This assignment might require you to do some research on your own. If you get stuck, try googling the problem, especially when it comes to importing and using the different modules.

# Hint you will want to enable word wrap in vscode (View -> Toggle Word Wrap) to make it easier to read the instructions.

# Question 1:
# Write a function that takes in a number and returns that number squared
# IE. If the user inputs 3, the function should return 9
def square_number(num):
    return num ** 2


# Question 2:
# Write a function that takes in a string, a letter, and a number and returns the string with the letter replaced at the number index
# IE. If the user inputs "Hello World", "a", and 3, the function should return "Helao World"
# Hint: You will want to use the replace() function
def replace_letter_at_index(string, letter, index):
    return string[:index] + letter + string[index+1:]
# Question 3:
# Write a function that takes in a number, a lower_bound, and an upper_bound and returns whether the number is within the bounds
# IE. If the user inputs 5, 1, and 10, the function should return True
def is_within_bounds(number, lower_bound, upper_bound):
    return lower_bound <= number <= upper_bound
# Question 4:
# write a function with parameters for a name, age, and favorite color. Return the following string using the parameters:
# "Hello, my name is <name>. I am <age> years old. My favorite color is <color>."
def generate_intro(name, age, color):
    return f"Hello, my name is {name}. I am {age} years old. My favorite color is {color}."

# Question 5:
# Write a function that asks the user for their name, age, and favorite color and then calls the function from question 4 using the user's input as the parameters.
# Hint: You will want to save the users input to variables and use them as the parameters for the function from question 4
def ask_user_and_generate_intro():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    color = input("Enter your favorite color: ")
    intro = generate_intro(name, age, color)
    print(intro)

# Question 6:
# import the random module and use it to generate a random number between 1 and 100
import random
random_number = random.randint(1, 100)
# Question 7:
# import the math module and use it to find the square root of 16 (hint: use the sqrt() function)
import math
square_root_of_16 = math.sqrt(16)
# Question 8:
# import the sys module and use it to print the version of python you are using
# this time import the module using the import "as" keyword
# hint: use the version attribute (sys.version)
import sys as system
python_version = system.version
# Question 9:
# import the os module and use it to print the current working directory. This time import the module using the from keyword
# hint: use the getcwd() function
from os import getcwd
current_working_directory = getcwd()
print(square_number(3))  # Question 1
print(replace_letter_at_index("Hello World", "a", 3))  # Question 2
print(is_within_bounds(5, 1, 10))  # Question 3
print(generate_intro("Alice", 30, "Blue"))  # Question 4
ask_user_and_generate_intro()  # Question 5
print(random_number)  # Question 6
print(square_root_of_16)  # Question 7
print(python_version)  # Question 8
print(current_working_directory)  # Question 9
