# James Morrissey
# computingID: jpm9rk


import random

num_to_guess = int(input('What should the answer be? '))
if num_to_guess == -1:
    num_to_guess = random.randrange(1, 101)
num_of_guess = int(input('How many guesses? '))

for i in range(num_of_guess):
    guess = int(input('Guess a number: '))
    if guess > num_to_guess:
        if i == num_of_guess-1:
            print('You lose; the number was', num_to_guess)
            break
        print('The number is lower than that.')
    elif guess < num_to_guess:
        if i == num_of_guess-1:
            print('You lose; the number was', num_to_guess)
            break
        print('The number is higher than that.')
    elif guess == num_to_guess:
        print('You win!')
        break
