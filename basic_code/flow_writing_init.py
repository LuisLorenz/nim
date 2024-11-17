import time
import sys

class flow_writing:
    def __init__(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)

            if char in ".!?":
                time.sleep(0.5) 
        print(' ') # adding a new row


text = 'Hello my friend ...'
introduction = flow_writing(text)

text = 'Long it has been ...'
main = flow_writing(text)

text = 'Have a nice day ...'
ending = flow_writing(text)

