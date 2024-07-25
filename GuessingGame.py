import random

print("Welcome to Number Guessing game \n")

num_guesses = 0
upper_bound = (input("Enter a number: "))

if upper_bound.isdigit():
  upper_bound = int(upper_bound)

  if upper_bound <= 0:
    print("Enter a positive number next time! ")
    quit()

else:
  print("Enter a number next time! ")
  quit()


random_number = random.randint(0,upper_bound)
print(random_number)

while True:
  num_guesses+=1
  user_guess = (input("Enter guess: "))

  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:
    print("Enter a number next time! ")
    continue

  if user_guess == random_number:
    print(f'you got it!! in {num_guesses} guesses! ' )
    break
  
  elif user_guess > random_number:
    print("Guess a little low!")
  elif user_guess < random_number:
    print("Guess a little higher!")
    
    
  
