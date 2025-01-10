import time
import random
import sys
from colorama import Fore, Back, Style

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

# def pile_illustration(pile):
#     five_elements = pile // 5 
#     single_elements = pile - (5 * five_elements)
#     pile_string = (five_elements * 'ooooo ') + (single_elements * 'o') 
#     if single_elements != 0: 
#         pile_string += ' '
#     return pile_string

def pile_illustration(pile):
    five_elements = pile // 5 
    single_elements = pile - (5 * five_elements)
    # pile_string = (five_elements * 'ooooo ') + (single_elements * 'o') 
    # if single_elements != 0: 
    #     pile_string += ' '
   
    # adding the color before the string is combined seems to be a good approach 
    # if statements seem to help here quite well I think 
    if five_elements == 1:
        pile_string = Fore.RED + 'ooooo ' + Fore.MAGENTA + single_elements * 'o' + Fore.RESET
    elif five_elements == 2:
        pile_string = Fore.RED + 'ooooo ' + Fore.MAGENTA + 'ooooo ' + Fore.BLUE + single_elements * 'o' + Fore.RESET
    elif five_elements == 3:
        pile_string = Fore.RED + 'ooooo ' + Fore.MAGENTA + 'ooooo ' + Fore.BLUE + 'ooooo ' + Fore.GREEN + single_elements * 'o' + Fore.RESET
    elif five_elements == 4:
        pile_string = Fore.RED + 'ooooo ' + Fore.MAGENTA + 'ooooo ' + Fore.BLUE + 'ooooo ' + Fore.GREEN + 'ooooo ' + Fore.RESET
    elif five_elements == 0:
        pile_string = Fore.RED + single_elements * 'o' + Fore.RESET
    return pile_string


        


def move(pile, is_maximizing, second_player, player_turn): 
    if is_maximizing: 
        best_move = minimax(pile, is_maximizing)
        take = best_move[1]
        text_computer_take = 'The '+ Fore.MAGENTA  + 'COMPUTER' + Fore.RESET + f' has taken {take} ...'
        flow_writing(text_computer_take)
        return take
    else: 
        if second_player == 1:
            text_player_turn = f"{player_turn} is on the turn."
            flow_writing(text_player_turn)
            text_current_pile = f'The pile has {pile} items ...'
            flow_writing(text_current_pile)
            pile_string = '*** ' + pile_illustration(pile) + '***'
            flow_writing(pile_string)
        else:
            text_current_pile = f'The current pile has {pile} items ...'
            flow_writing(text_current_pile)
            pile_string = '*** ' + pile_illustration(pile) + '***'
            flow_writing(pile_string)

        valid_take = False
        while valid_take == False: 
            take_options = []
            for x in range(1, min(pile, 3) + 1):
                take_options.append(x)
            text_take = f'Select a take: {take_options}: '
            flow_writing(text_take)
            take = int(input('>> '))
            if take in range(1, min(pile, 3) + 1):
                valid_take = True
                return take
            else:
                text_invalid = '''Your input was invalid ... 
Please try again ...'''
                flow_writing(text_invalid)

class flow_writing:
    def __init__(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01) # 0.05

            if char in ".!?":
                time.sleep(0.01) # 0.2
        print(' ') 

def game():
    global score_player_1, score_player_2, score_human_player, score_computer_player
        
    min_value = 7
    max_value = 20 
        # pile: ooooo (red) ooooo (orange) ooooo (lila) ooooo (blue)
    pile = random.randint(min_value, max_value)
    initial_pile = pile 
    
    winner = None

    # understandable varibales 
    human__vs_computer = [True, False]
    human_vs_human = ["PLAYER 1", "PLAYER 2"]
    player_turn = None
    is_maximizing = None 

    # random starting player
    if second_player == 1:  
        player_turn = random.choice(human_vs_human)

        #here I can change the color depending on the outcome
        if player_turn == "PLAYER 1":
            player_turn = Fore.BLUE + "PLAYER 1" + Fore.RESET
        if player_turn == "PLAYER 2":
            player_turn = Fore.RED + "PLAYER 2" + Fore.RESET

    else: 
        is_maximizing = random.choice(human__vs_computer)
  

    while pile != 0:
        
        # mode human player vs human player
        if second_player == 1: 

            

            take = move(pile, is_maximizing, second_player, player_turn)
            pile = pile - take 
            if player_turn == Fore.BLUE + "PLAYER 1" + Fore.RESET: # var must be in the same color and style to be really the same 
                player_turn = Fore.RED + "PLAYER 2" + Fore.RESET
            else:
                player_turn = Fore.BLUE + "PLAYER 1" + Fore.RESET

            pass
        # mode human player vs computer 
        else: 
            if is_maximizing == True: 
                if initial_pile == pile:
                    text_current_pile = f'The inital pile has {pile} items ...'
                    flow_writing(text_current_pile)
                    pile_string = '*** ' + pile_illustration(pile) + '***'
                    flow_writing(pile_string)

            take = move(pile, is_maximizing, second_player, player_turn)
            pile = pile - take 
            if is_maximizing:
                is_maximizing = False
            else:
                is_maximizing = True 

    if second_player == 1: 
        if player_turn == "PLAYER 1":
            t_win = Fore.RED + 'PLAYER 2 ' + Fore.RESET + '''took the last element ...
And won this game, congrates! ...'''
            flow_writing(t_win)
            score_player_2 += 1
        else: 
            t_win = Fore.BLUE + 'PLAYER 1 ' + Fore.RESET + '''took the last element ...
And won this game, congrates! ...'''
            flow_writing(t_win)
            score_player_1 += 1
    else:      
        if not is_maximizing: 
            t_loss = "The " + Fore.MAGENTA + "COMPUTER " + Fore.RESET + """took the last element ...
I'm sorry, you lost the game!""" 
            flow_writing(t_loss)
            
            score_computer_player += 1 
        else:
            t_win = Fore.BLUE + 'You ' + Fore.RESET + '''took the last element ...
Congrates, you won this game!'''
            flow_writing(t_win)
            
            score_human_player += 1

score_player_1 = 0 
score_player_2 = 0
score_human_player = 0 
score_computer_player = 0  

def score_board(second_player):
    if second_player == 1:
        t_score_board = f"""
############################

Score board: 
""" + Fore.BLUE + "PLAYER 1" + Fore.RESET + """: {score_player_1}
""" + Fore.RED + "PLAYER 2" + Fore.RESET + """: {score_player_2}

############################
"""
    else: 
        t_score_board = f"""
############################

Score board: 
""" + Fore.BLUE + "HUMAN" + Fore.RESET + """: {score_human_player}
""" + Fore.MAGENTA + "COMPUTER" + Fore.RESET + """: {score_computer_player}

############################
"""
    flow_writing(t_score_board)


intro = '''
Welcome to NIM! ...
Do you really think you can beat the computer? ...
HA HA HA ...
Let's go! ...
These are the rules ... 
>> Minimal take is 1 element ...
>> Maximal take are 3 elements ...
>> The player who takes the last element wins ... 
'''

# choosing a game mode 
second_player = None 
while second_player == None: 
    second_player_text = """Choose your OPPONENT: ...
Type '1' for """ +Fore.BLUE + "HUMAN" + Fore.RESET + """ ...
Type '2' for """ + Fore.MAGENTA  + "COMPUTER" + Fore.RESET + " ..."
    flow_writing(second_player_text)
    second_player = int(input('>> '))
    if second_player == 1 or 2: 
        continue 
    else: 
        text_invalid = 'Your input was unvalid. Please try again.'
        flow_writing(text_invalid)
        second_player = None 

is_maximizing = False
super_loop = True 
while super_loop == True: 
    game() 
    score_board(second_player)
    play_again = None
    while play_again == None: 
        text_play_again = 'Do you want to play again? (y/n): '
        flow_writing(text_play_again) 
        play_again = input('>> ')
        if play_again == 'y':

            # is this for changing the player? No necessary anymore? 
            if is_maximizing:
                is_maximizing = False 
            else:
                is_maximizing = True 
            continue
        elif play_again == 'n':
            super_loop = False
        else: 
            text_invalid = 'Your input was unvalid. Please try again.'
            flow_writing(text_invalid)
            play_again = None

    
    