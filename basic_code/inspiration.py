    # minimax_simplenim.py

def minimax(state, max_turn):
    if state == 0:
        return 1 if max_turn else -1

    possible_new_states = [
        state - take for take in (1, 2, 3) if take <= state
    ]
    # smarte to exclude this algorithm 
    # because it works for the turn of the user and the computer

    if max_turn:
        scores = [
            minimax(new_state, max_turn=False)
            for new_state in possible_new_states
        ]
        return max(scores)
    else:
        scores = [
            minimax(new_state, max_turn=True)
            for new_state in possible_new_states
        ]
        return min(scores)