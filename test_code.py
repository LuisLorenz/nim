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