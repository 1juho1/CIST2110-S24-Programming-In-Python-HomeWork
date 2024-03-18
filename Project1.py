# Project1.py
# Author: Justin Hoang


# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions
def welcome_message():
    print("Welcome to the Quiz Game!")
    print("You will be asked a series of questions. Choose the correct answer from the options provided.")
    print("Let's get started!\n")

def ask_question(question, options, correct_answer):
    print(question)
    for idx, option in enumerate(options):
        print(f"{chr(97+idx)}) {option}")
    user_answer = input("Your answer (a, b, c, or d): ").lower()
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        print(f"The correct answer is: {correct_answer}")
        return False

def display_final_score(score):
    print(f"\nYour final score is: {score}/5")
    print("Thank you for playing!")

def main():
    questions = [
        ("What is the capital of France?",
         ["Paris", "Rome", "Madrid", "Berlin"],
         "a"),
        ("Which planet is known as the Red Planet?",
         ["Jupiter", "Venus", "Mars", "Saturn"],
         "c"),
        ("Who wrote 'Romeo and Juliet'?",
         ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
         "a"),
        ("What is the chemical symbol for water?",
         ["H2O", "CO2", "NaCl", "O2"],
         "a"),
        ("Which is the largest mammal?",
         ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
         "b")
    ]

    score = 0

    welcome_message()

    for question, options, correct_answer in questions:
        print("\n----------------------------------")
        if ask_question(question, options, correct_answer):
            score += 1

    display_final_score(score)

if __name__ == "__main__":
    main()
# Quiz Game:
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.

# Write a function that displays a welcome message to the user and explains the rules of the game

# Implement at least 5 questions, each with 4 answer options (a, b, c, d). Each question should be worth 1 point.
# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
# Use if or if-else statements to check if the answer is correct.
# If the answer is correct, display a positive feedback message and add points to the user's score.
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
# Score Tracking:

# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
# Function Utilization:

# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, the correct answer, and return whether the user was correct.
# an example would be def ask_question(question:str, option_1:str, option_2:str, option_3,:str option_4:str, correct_answer:str)->bool:
# the return value should be a boolean (True or False) for whether the user was correct

# Create a function to display the final score, which takes the score as a parameter and displays a message.
# Loops:
# Use a for or while loop to iterate through the questions.
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d).
