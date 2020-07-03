import random


def coin_flip():
    #define coins
    coins = ['heads', 'tails']
    #start a list to record all coin flips
    flipped = []
    #allow user to enter the number of times to flip
    number = int(input('Please enter a number of times you would like to flip the coin: '))
    while number < 1:
        number = int(input('Invalid number, please retry: '))
        return number
    else:
        print('You have chosen to flip', number, 'times')

    #append to the empty "flipped" list to record coin tosses
    for num in range(0, number):
        flipped.append(random.choice(coins))
    print(flipped)

    #count the number of heads or tails in "flipped" and record as variables
    heads = flipped.count('heads')
    tails = flipped.count('tails')
    print("The number of heads is:", heads)
    print("The number of tails is:", tails)

    #display the winner
    for flip in flipped:
        if heads > tails:
            return "heads won"
        elif tails > heads:
            return "tails won"
        else:
            return "tie"
            