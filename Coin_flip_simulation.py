import random

heads = 0
tails = 0

coin_sides = ['Heads','Tails']

while True:
    
    choose = input('Do you want to flip a coin: YES / NO')
    if choose[0].lower() == 'y':
        flip = random.choice(coin_sides)
        if flip == coin_sides[0]:
            heads +=1
            print('\nHeads!')
        else:
            tails +=1
            print('\nTails!')
    else:
        print('\nHeads - {0}\nTails - {1}'.format(heads,tails))
        break
