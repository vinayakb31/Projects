# Rock, paper, scissors game

import random

print('''
Welcome to Rock Paper Scissors!
Rock wins against scissors, paper wins against rock, and scissors wins against paper.
You will get three chances.
''')
print('Do you want to play Rock Paper Scissor?\n1. Yes\n2. No')
print('\nEnter the number\n---------------------')
a = int(input())
moves = ['Rock', 'Paper', 'Scissor']
again = 1

while a>2 or a<1:
    a = int(input('Enter valid input: '))

if a == 2:
    print('Sorry to see you go :(')
elif a == 1:
    while again == 1:
        r = 1
        x = 0
        for a in range(3):
            move_ai = random.choice(moves)
            print('\nEnter your move for round', r, '\n  1. Rock\n  2. Paper\n  3. Scissor')
            i = int(input())
            while i>3 or i<1:
                i = int(input('Enter a valid input: '))
            
            if i == 1:
                move_player = 'Rock'
            elif i == 2:
                move_player = 'Paper'
            elif i == 3:
                move_player = 'Scissor'
            
            if move_player == move_ai:
                res = 'Tie'
                print('You both played', move_ai, 'in round', r)
            elif move_player == 'Rock' and move_ai == 'Paper':
                res = 'Win'
                print('The opponent played', move_ai)
                print('You Win round', r)
            elif move_player == 'Paper' and move_ai == 'Rock':
                res = 'Lose'
                print('The opponent played', move_ai)
                print('You Lose round', r)
            elif move_player == 'Scissor' and move_ai == 'Paper':
                res = 'Win'
                print('The opponent played', move_ai)
                print('You Win round', r)
            elif move_player == 'Paper' and move_ai == 'Scissor':
                res = 'Lose'
                print('The opponent played', move_ai)
                print('You Lose round', r)
            elif move_player == 'Rock' and move_ai == 'Scissor':
                res = 'Win'
                print('The opponent played', move_ai)
                print('You Win round', r)
            elif move_player == 'Scissor' and move_ai == 'Rock':
                res = 'Lose'
                print('The opponent played', move_ai)
                print('You Lose round', r)

            if res == 'Win':
                x+1 
            elif res == 'Tie':
                x+0.5 

            r = r+1
        
        print('\n------------')

        if x >= 2:
            print('\nYou Won the Game!')
        elif x == 1.5:
            print("It's a tie!")
        else:
            print('\nYou Lost the Game!')
    
        print('Do you want to play again?\n  1. Yes \n  2. No')
        again = int(input())

print('Thanks for playing!')