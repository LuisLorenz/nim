pile = 12
# take_options = [(x for x in range(1, min(pile, 3) + 1))]
take_options = []
for x in range(1, min(pile, 3) + 1):
    take_options.append(x) # [1, 2, 3]
print(take_options)

def test():
    if False:
        print('True')
    else: 
        print('False')
    print('End')

test()

for take in range(1, min(pile, 3) + 1):
     print(take)
     print(type(take))

scores = []  # super_list
for take in range(1, min(pile, 3) + 1):
    # new_pile = pile - take
    scores.append(((pile - take),(take)))
print(scores)

score_player_1 = 0 
score_player_2 = 0 
 
def score_board():
    print(f"""
score board 
player 1: {score_player_1}
player 2: {score_player_2}
""")

pile = 7   
for x in range(0, pile + 1):
    print('o', end='')
    