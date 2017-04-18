from random import randint

def roll_die(dice):
    return (randint(1, dice))

def roll_dice(number, dice):
    results = []
    for i in range(number):
        results.append(roll_die(dice))

def check_dice(input):
    if 'd' in input:
        input = input.split('d')
        d = int(input[0])
        n = int(input[1])
        return roll_dice(d,n)
    else:
        return roll_die(input)
