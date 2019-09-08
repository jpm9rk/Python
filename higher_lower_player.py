# James Morrissey
# computingID: jpm9rk
# Implementation of a guessing game

print("Think of a number between 1 and 100 and I'll guess it.")
num_guess = int(input('How many guesses do I get? '))
low_range = 1
high_range = 100
higher_than = 1
lower_than = 100
for i in range(num_guess):
    guess = (high_range + low_range)//2
    clue = input('Is the number higher, lower, or the same as ' + str(guess) + '? ')
    if clue == 'lower':
        lower_than = guess
        high_range = guess - 1
    if clue == 'higher':
        low_range = guess + 1
        higher_than = guess
    if clue == 'same':
        print('I won!')
        break
    if abs(higher_than - lower_than) == 1:
        print('Wait; how can it be both higher than', higher_than, 'and lower than ' + str(lower_than) + "?")
        break
    if i == num_guess - 1:
        user_num = int(input('I lost; what was the answer? '))
        if user_num >= lower_than:
            print("That can't be; you said it was lower than " + str(lower_than))
        if user_num <= higher_than:
            print("That can't be; you said it higher than " + str(higher_than))
        else:
            print('Well played!')


