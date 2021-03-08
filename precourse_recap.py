import random

secret_number=random.randrange(0,99)

print('Guess what number I am thinking of from 0 - 99?')


while True:
    number_guess = eval(input('Enter number:'))
    if number_guess == secret_number:
        print ('\nWow!!! How did you know!?')
        break

    elif number_guess > secret_number:
        print('\nToo high, nice try. Try again.')
        
    elif number_guess < secret_number:
        print('\nToo low, some way to go. Try again.')