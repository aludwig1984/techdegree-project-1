import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    random_number = random.randint(1, 100)
    number_of_guesses = 1

    try:
        user_guess = int(input("Please choose a number between 1 and 100 "))
        while user_guess > int(100):
            user_guess = int(input("Number needs to be 100 or lower "))
            number_of_guesses = number_of_guesses + 1
        while user_guess < int(1):
            user_guess = int(input("Number needs to be 1 or higher "))
            number_of_guesses = number_of_guesses + 1
        while user_guess > random_number:
            user_guess = int(input("It's lower "))
            number_of_guesses = number_of_guesses + 1
        while user_guess < random_number:
            user_guess = int(input("It's higher "))
            number_of_guesses = number_of_guesses + 1
        if user_guess == random_number:
            print("Got it. It took you", number_of_guesses, "tries. Have a nice day!")
    except ValueError:
        print("Oh no! We ran into an error. Please try again.")

start_game()
