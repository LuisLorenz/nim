def minimax(pile, is_maximizing):
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
        score = 0 
        for take in range(1, min(pile, 3) + 1):
            # min = 1
            # max = 3 =< plie 
            minimax(pile - take, is_maximizing=True)

    pass 