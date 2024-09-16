import random

while True:
    roll = input('Roll the dice [y/n]: ')
    if roll == 'y':
        print(f"Dice rolled: {random.randint(1, 6)}")
    else:
        break
