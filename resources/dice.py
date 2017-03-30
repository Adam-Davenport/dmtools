from random import randint

def roll_die(dice):
    return (randint(1, dice))

def roll_dice(number, dice):
    results = []
    for i in range(number):
        results.append(roll_die(dice))
