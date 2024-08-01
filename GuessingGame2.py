import random

def get_upper_bound():
    while True:
        upper_bound = input("Enter the upper bound: ")
        if upper_bound.isdigit():
            upper_bound = int(upper_bound)
            if upper_bound > 0:
                return upper_bound
            else:
                print("Enter a positive number! ")
        else:
            print("Type a number! ")

def get_guess():
    while True:
        user_guess = input("Enter your guess: ")
        if user_guess.isdigit():
            return int(user_guess)
        else:
            print("Type a number! ")

def main():
    print("Welcome to the Number Guessing Game!")
    upper_bound = get_upper_bound()
    random_number = random.randint(1, upper_bound)
    num_guesses = 0

    while True:
        num_guesses += 1
        user_guess = get_guess()

        if user_guess == random_number:
            print(f"You got it right in {num_guesses} guesses!")
            break
        elif user_guess > random_number:
            print("Guess a little lower! ")
        else:
            print("Guess a little higher!")

if __name__ == "__main__":
    main()
