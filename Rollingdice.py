 # Dice Roller Simulator
# Description: This project simulates rolling a dice. Each time the user runs the program, it generates a random number between 1 and 6 — just like a real dice!

import random

def roll_dice():
    x = True
    print('Dice Roller Game')
    while x:
        y = input('Press Enter "Y" to roll the dice or type "q" to quit: ').lower()
        if y == 'y':
            dice = random.randint(1,6)
            print(f'You rolled a {dice}!\n')
        else:
            print('Wrong Input, please try again')
        choice = input('Roll again? (y/n): ').lower()
        if choice != 'y':
            print('Thanks for playing!')
            x = False
            

roll_dice()
                






