import time
import random
import sys

# is_maximizing -> computer player
# is minimizing -> human best player 

def minimax(pile, is_maximizing):
    if pile == 0:
        return (1 if is_maximizing == False else -1, None) 
    
    if is_maximizing: 
        scores = []  
        for take in range(1, (min(pile, 3) + 1)):
            result, _ = minimax(pile - take, is_maximizing=False)
            score = (result, take)
            scores.append(score)
        return max(scores, key=lambda x: x[0]) 

    else:
        scores = [] 
        for take in range(1, (min(pile, 3) + 1)): 
            result, _ = minimax(pile - take, is_maximizing=True)
            score = (result, take)
            scores.append(score)
        return min(scores, key=lambda x: x[0]) 

def move(pile, is_maximizing): 
    if is_maximizing: 
        best_move = minimax(pile, is_maximizing)
        take = best_move[1]
        print(f'The computer has taken {take}.')
        return take
    else: 
        print(f'The current pile has {pile} items.' )
        valid_take = False
        while valid_take == False: 
            take_options = []
            for x in range(1, min(pile, 3) + 1):
                take_options.append(x)
            take = int(input(f'Select a take: {take_options}: '))
            if take in range(1, min(pile, 3) + 1):
                valid_take = True
                return take
            else:
                print('Your input was invalid. Please try again.')

class flow_writing:
    def __init__(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)

        if char in ".!?":
            time.sleep(0.5) 
        print(' ') # adding a new row

intro = '''
Welcome to NIM!
Do you really think you can beat the computer?
Ha Ha Ha
Let's go!
'''

rules = """
Here are the rules 
- there are a certain amount of items in a pile
- each player take minimally one time and maximally 3 times per turn
- the game ends when the pile reaches zero items 
- the player that takes the last item of the pile wins
"""

def game():
    # var
    global score_player_1, score_player_2
        # global var
            # so when I change the value of the var in this func the value is changed globally (even outside this func)
    pile = 12 # random pile selection
              # avoiding the pile amount that was chosen before
    winner = None
    is_maximizing = False

    # game loop
    while pile != 0:
        
        take = move(pile, is_maximizing)
        pile = pile - take 
        if is_maximizing:
            is_maximizing = False
        else:
            is_maximizing = True 

    # end 
    if not is_maximizing: 
        print("I'm sorry, you lost the game!")
        score_player_2 += 1 
    else:
        print('Congrates, you won this game.')
        score_player_1 += 1

score_player_1 = 0 
score_player_2 = 0 

def score_board():
    print(f"""
score board: 
  player 1: {score_player_1}
  player 2: {score_player_2}
""")


# first game
    # having the intro & rules just once

# flow_intro = flow_writing(intro)
# flow_rules = flow_writing(rules)

# super game loop
is_maximizing = False
super_loop = True 
while super_loop == True: 
    game()
    score_board()
    play_again = None
    while play_again == None: 
        play_again = input('Do you want to play again? (y/n): ')
        if play_again == 'y':
            # between each game alternate the starting player 
            if is_maximizing:
                is_maximizing = False 
            else:
                is_maximizing = True 
            continue
        elif play_again == 'n':
            super_loop = False
        else: 
            print('Your input was unvalid. Please try again.')
            play_again = None

    
    