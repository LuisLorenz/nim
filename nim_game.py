# player
    # is_maximizing -> computer player
    # is minimizing -> human best player 

def minimax(pile, is_maximizing):
    # this func returns the max/min score
    # check for empty pile 
        # pile == 0, player = X
        # player x is winner because player y took the last item the turn before
    if pile == 0:
        return 1 if is_maximizing else -1
    
    # loop to go through all potential takes 
    if is_maximizing: 
        scores = 0 
        for take in range(1, min(pile, 3) + 1):
            # min = 1
            # max = 3 =< plie 
            scores = [minimax(pile - take, is_maximizing=False)]
        return max(scores)
    else:
        score = 0 # or '- inf'
        for take in range(1, min(pile, 3) + 1):
            # min = 1
            # max = 3 =< plie 
            minimax(pile - take, is_maximizing=True)
        return min(scores)

def move(pile, is_maximizing): 
    if is_maximizing: 
        # minimax ...
        pass
    else: 
        print(f'The current pile has {pile} items.' )
        valid_take = False
        while valid_take == False: 
            take = input('How much do you want to take?: ')
                # form a list with options that the user has with nice formating
            if take in range(1, min(pile, 3) + 1):
                return valid_take == True
            else:
                print('Your input was invalid. Please try again.')
    pile = pile - take
    if pile == 0:
        if is_maximizing:
            winner = 'user'
        else: 
            winner = 'computer'
    # create a game loop in the game func



def game():
    # intro
    print('Welcome to NIM!')
    print('Do you really think you can beat the computer?')
    print('Ha Ha Ha')
    print("Let's go!")

    # var
    pile = 12 
    is_maximizing = False 
    winner = None

    # game loop
    while pile != 0:
        move(pile, is_maximizing)

    # end 
    if winner == is_maximizing: 
        print("I'm sorry, you lost the game!")
    else:
        print('Congrates, you won this game.')

# super game loop
while True: 
    game()
    play_again = input('Do you want to play again? (y/n): ')
    if play_again == 'y':
        continue
    else:
        break 
    