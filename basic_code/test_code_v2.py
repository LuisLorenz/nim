piles = 7   
for x in range(0, piles+ 1):
    print(' o ', end='')
print(' ')

# printing in groups
# using math this way
# groups
    # ooooo ooooo ooooo oo 
    # 7 / 5 = 1 
    # 7 % 5 = 2 or 7 - 5 = 2, print ... 

var = 7 / 5 
print(var)
var = 7 // 5 
print(var)
# so I need this 

pile = 7
five_elements = None 
single_elements = None 
five_elements = pile // 5 
single_elements = pile - (5 * five_elements)
# for x in range(0, piles+ 1):
    # five_elements * 'ooooo ' 
    # single_elements * 'o' 
    # print('o', end='')
    # The end='' argument ensures that the next output is printed on the same line, rather than starting a new line after each iteration.

pile_string = (five_elements * 'ooooo ') + (single_elements * 'o')
print(pile_string)

pile = 25
five_elements = pile // 5 
single_elements = pile - (5 * five_elements)
pile_string = (five_elements * 'ooooo ') + (single_elements * 'o')
print(pile_string)

