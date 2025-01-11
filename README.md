[## principle ](https://realpython.com/python-minimax-nim/)

## plan 
-[x] seeing the computer has made a move 
-[x] implement the nice illustration of flow writing fully  
-[x] random pile choice
    - pile_options = [12, 15, 9]
    - better: a radome number in a range (10-20) 

## plan v3
-[x] player vs player choice 
    - choosing between playing again AI or not 
    - yes or no questition
            - select "player" or "computer" 
    - creating game_1 & game_2 would work but would be copy code 
    - better to have just one game >> better performance 
-[x] record counter
-[-] changing rules (randomly) -> do this maybe for a different game 
    - making it harder with time pressure to force people to make a quick decision
-[x] continue here: implement illustrations with o's as item amount in pile
    - pile of 7:
        ooooo oo
    - pile of 15:
        ooooo ooooo ooooo

        for x in pile:
            print('o')
-[x] making  the game more challenging with multiple piles
    - research how to make this game more advanced
-[x] random player that starts the game 
-[x] bug fixing: mode = 1, alternating player
-[x] improve illustration
... 

## plan v4
-[-] giving my code to AI for evaluation and improvement 
    - doing this with segementation
    - prompt:
        I have programed the game of 'Nim' in python successfully. Here is a part of my code. Please give me adive how I can improve it to make it more efficient. Explain me your adive: 
    -[ ] minimax
    -[ ] pile illustration 
    -[ ] move
    -[ ] flow writing
    -[ ] game 
    -[ ] score board
    -[ ] loop 
    -[ ] colors
-[-] implement time pressure! important





