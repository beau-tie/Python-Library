#This is a script that allows tow players to place the matching penny game until
#either player wins, then stops the game if requested.

from games import *

display_message()

i = raw_input("Choose either p or q: ")

while i != "q":
    pn1 = place_penny()
    print "Player 1: ", pn1
    pn2 = place_penny()
    print "Player 2: ", pn2
    while pn1 != pn2:
        print "Game continues..."
        pn1 = place_penny()
        print "Player 1: ", pn1
        pn2 = place_penny()
        print "Player 2: ", pn2

    if pn1 == "Heads":
        print "Player 1 wins the game!"
    else:
        print "player 2 wins the game!"

    display_message()

    i = raw_input("Choose either p or q: ")

print "Bye!"
