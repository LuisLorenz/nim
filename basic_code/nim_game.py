import time
import random
import sys

# player
    # is_maximizing -> computer player
    # is minimizing -> human best player 

def minimax(pile, is_maximizing):
    # this func returns the max/min score
    # check for empty pile 
        # pile == 0, player = X
        # player y is winner because player y took the last item the turn before
    if pile == 0:
        return 1 if is_maximizing == False else -1
    
    # loop to go through all potential takes 
    if is_maximizing: 
        scores = []  # super_list
        for take in range(1, (min(pile, 3) + 1)):
            # min = 1
            # max = 3 =< plie 
            result = minimax(pile - take, is_maximizing=False)
            score = (result, take) # ((x)(y))
        print(score)
        return max(scores, key=lambda x: x[0]) 
    
    # max_element = max(your_list, key=lambda x: x[0])
    #   max() on first element of the tuple [x[0]]

    else:
        scores = [] 
        for take in range(1, (min(pile, 3) + 1)): 
            score = ((minimax(pile - take, is_maximizing=False)),(take))
            print(score)
            scores.append(((minimax(pile - take, is_maximizing=True)),(take)))
        print(scores)
        return min(scores, key=lambda x: x[0]) 

    # transform the score into a take
    # dictionary seems to be reasonable or tuple 
    # tuple = (0,0)
    # super_list = [(0,0), (1,0), (0,1)]
    # print(super_list[1][0]) -> "1" = take 

    # setting
        # ((take)(score))
    # creation
        # simple a super_list
        # append simply the tuple -> easy
    # access -> ok 
    # switching to ((score)(take)) should make the max/min search simpler 

def move(pile, is_maximizing): 
    if is_maximizing: 
        score_take = minimax(pile, is_maximizing)
        for x in range(1,2):
            take = x 
    else: 
        print(f'The current pile has {pile} items.' )
        valid_take = False
        while valid_take == False: 
            # take_options = [(take for take in range(1, min(pile, 3) + 1))]
            take_options = []
            for x in range(1, min(pile, 3) + 1):
                take_options.append(x)
            take = int(input(f'Select a take: {take_options}: '))
                # form a list with options that the user has with nice formating
            if take in range(1, min(pile, 3) + 1):
                # valid_take = True 
                # return valid_take
                # return True
                # Once a return statement is executed, the function exits, and any code after it will not run.
                valid_take = True
            else:
                print('Your input was invalid. Please try again.')
    pile = pile - take # return pile?
    # print('valid input')
    # return pile

def intro():
    print('Welcome to NIM!')
    time.sleep(0.2)
    print('Do you really think you can beat the computer?')
    time.sleep(0.2)
    print('Ha Ha Ha')
    time.sleep(0.2)
    print("Let's go!")

def rules():
    print('''Here are the rule: 
- there are a certain amount of items in a pile
- each player take minimally one time and maximally 3 times per turn
- the game ends when the pile reaches zero items 
- the player that takes the last item of the pile wins
          ''')

def game():
    # var
    pile = 12 # random pile selection
              # avoiding the pile amount that was chosen before
    winner = None
    is_maximizing = False

    # game loop
    while pile != 0:
        move(pile, is_maximizing)
        if is_maximizing:
            is_maximizing = False
        else:
            is_maximizing = True 

    # end 
    if winner == is_maximizing: 
        print("I'm sorry, you lost the game!")
    else:
        print('Congrates, you won this game.')

# first game
    # having the intro & rules just once
intro()
rules()

# super game loop
is_maximizing = False 
while True: 
    game()
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
            break # or retur False
        else: 
            print('Your input was unvalid. Please try again.')
            play_again = None

    
    