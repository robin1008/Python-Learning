'''
I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low. Take a guess.
17
Your guess is too high. Take a guess.
16
Good job! You guessed my number in 4 guesses!
'''

import random

def guess():
    try:
        print('I am thinking of a number between 1 and 20')
        randomNum = random.randint(1,5)
        print('Random Number is：',randomNum)

        for guessTime in range(1,100):
            print('Take a guess.')
            guessNum = int(input('Please input your guess number:'))
            if guessTime > 5:
                print('【【【your can''t guess more times!】】】')
                return False
            else:
                if guessNum < randomNum:
                    print('your guess is too low.')
                    #continue
                elif guessNum > randomNum:
                    print('your guess is too high.')
                elif guessNum == randomNum:
                    print('Good Job! you guessed my number in' + ' ' + str(guessTime) + ' ' + 'guess!')
                    return True
    except ValueError:
        print('Please input a right number!')
guess()


