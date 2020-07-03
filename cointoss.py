import random


def coin_flip():
    
    coins = ['heads', 'tails']
    flipped = []
    number = int(input('Please enter a number of times you would like to flip the coin: '))
    while number < 1:
        number = int(input('Invalid number, please retry: '))
        return number
    else:
        print('You have chosen to flip', number, 'times')
    
    for num in range(0, number):
        flipped.append(random.choice(coins))
    print(flipped)

    heads = flipped.count('heads')
    tails = flipped.count('tails')
    print("The number of heads is:", heads)
    print("The number of tails is:", tails)
    for flip in flipped:
        if heads > tails:
            return "heads won"
        elif tails > heads:
            return "tails won"
        else:
            return "tie"
            