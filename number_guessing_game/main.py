# Basic Python script: Number guessing program
import random

def enter_number():
    print("Number Guessing Game! 👋")
    number = int(input("Enter a number between 1 and 10: "))
    print(f"You entered: {number}!")
    return number

def random_number():
    return random.randint(1, 10)

def check_match(user_number, generated_number):
    if user_number == generated_number:
        print(f"🎉 You guessed it right!The correct number was {generated_number}")
    else:
        print(f"❌ Nope! The correct number was {generated_number}.")

# Main game flow
user_num = enter_number()
rand_num = random_number()
check_match(user_num, rand_num)
