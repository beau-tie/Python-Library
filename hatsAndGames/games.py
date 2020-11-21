# This is a function that uses the random function to pick a number between 1
# and 10, then determines whether the number is even or odd

from random import randint

def place_penny():
    r = randint(1, 10)
    if r % 2 == 0:
        return "Heads"
    else:
        return "Tails"

def display_message():
    print "###MENU###"
    print "p) Play the matching penny game."
    print "q) Quit."
        
