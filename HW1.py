# HW1.py
# Author: Justin Hong

# Question 1:
# Print Hello World like we did in class
print("Hello World")
# Question 2:
# Print the following:
# Your name
print("Justin Hoang")
# Your age
print("18")
# Your favorite color
print("red")
# Your favorite animal
print("otters")
# Question 3:
# Create a variable called "myName" and set it equal to your name
myName = "Justin Hoang"
# Create a variable called "myAge" and set it equal to your age
myAge = 18
# Create a variable called "myColor" and set it equal to your favorite color
myColor = "red"
# Create a variable called "myAnimal" and set it equal to your favorite animal
myAnimal = "otter"
# Print the following:
# Hello, my name is <myName>
# I am <myAge> years old
# My favorite color is <myColor>
# My favorite animal is <myAnimal>
print("Hello, my name is "+ myName +"" )
print("I am "+str(myAge)+" years old ")
print("My favorite color is "+myColor+"")
print("My favorite animal is "+myAnimal+"")
# Question 4:
# Calculate the following and print the result:
# 2 + 2
print(2+2)
# 3 * 4
print(3*4)
# 5 - 6
print(5-6)
# 8 / 2
print(8/2)
# Question 5:
# Create a variable called "num1" and set it equal to 2
num1 = 2
# Create a variable called "num2" and set it equal to 3
num2 = 3
# Create a variable called "num3" and set it equal to 4
num3 = 4
# Create a variable called "num4" and set it equal to 5
num4 =5
# Calculate the following and print the result:
# num1 + num2
print(num1+num2)
# num3 * num4
print(num3*num4)
# num4 - num1
print(num4-num1)
# num2 / num1
print(num2/num1)
# Question 6: Write a program that asks the user for their name and then prints the following:
name = input("Hello, please enter your name: ")
# Hello, <name>. Please enter three numbers.

# The program should then ask the user for three numbers (floats) and print the following:
print(f"Hello, {name}. Please enter three numbers:")
number1 = float(input("Number 1: "))
number2 = float(input("Number 2: "))
number3 = float(input("Number 3: "))

# 1. The sum of the three numbers is <sum>
sum = number1+number2+number3
print(f"The sum of the three numbers is {sum}")
# 2. The product of the three numbers is <product>
product = number1*number2*number3
print(f"The product of the three numbers is {product}")
# 3. round the three numbers to the nearest integer and print the sum of the three rounded numbers divided by 3
rounded_sum = round(num1) + round(num2) + round(num3)
print(f"3. The sum of the rounded numbers divided by 3 is {rounded_sum / 3}")
# 4. The average of the three numbers is <average>
average = sum / 3
print(f"4. The average of the three numbers is {average}")
# Question 7: Ask the user for an input of a symbol (in the example its *)
# Print a diamond of the symbol that looks like the following. Include the spaces and the | character.
# Hint: the print("symbol", end="") with \t and \n characters will be useful here.
symbol = input("\nEnter a symbol: ")
print("\nDiamond:")
for i in range(1, 6):
        print(" " * (5 - i) + symbol * (2 * i - 1))
for i in range(4, 0, -1):
        print(" " * (5 - i) + symbol * (2 * i - 1))

#    *     |
#   ***    |
#  *****   |
# *******  |
#  *****   |
#   ***    |
#    *     |
