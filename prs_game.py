import random

print('Welcome, hooman!')
print('Let\'s play Paper/Rock/Scissors')
print('Press 1 for Paper')
print('Press 2 for Rock')
print('Press 3 for Scissors')
print()
app = random.randint(1,3)
if app == 1:
    game = 'Paper'
elif app == 2:
    game = 'Rock'
else:
    game = 'Scissors'

try:
    x = int(input('Choose your option: '))
    if x == 1:
        print()
        print('Your choice is Paper')
        print('I choose ' + str(game))
        if app == 1:
            print('Draw! Let\'s play again')
        elif app == 2:
            print('Damn it! You won...')
        else:
            print('Ha-ha, you looser!')
    elif x == 2:
        print()
        print('Your choice is Rock')
        print('I choose ' + str(game))
        if app == 1:
            print('Ha-ha, you looser!')
        elif app == 2:
            print('Draw! Let\'s play again')
        else:
            print('Damn it! You won...')
    else:
        print()
        print('Your choice is scissors')
        print('I choose ' + str(game))
        if app == 1:
            print('Damn it! You won...')
        elif app == 2:
            print('Ha-ha, you looser!')
        else:
            print('Draw! Let\'s play again')
except:
    print('Type numbers only, you fool!')


