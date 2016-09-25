import random

print("Pick if the next card will be Higher, Lower, or the Same\n")

deck = [
'♥01-ace-01♥','♥02-two-02♥','♥03-three-03♥', '♥04-four-04♥','♥05-five-05♥',
'♥06-six-06♥','♥07-seven-07♥','♥08-eight-08♥','♥09-nine-09♥','♥10-ten-10♥',
'♥11-jack-11♥','♥12-queen-12♥','♥13-king-13♥','♠01-ace-01♠','♠02-two-02♠',
'♠03-three-03♠','♠04-four-04♠','♠05-five-05♠','♠06-six-06♠','♠07-seven-07♠',
'♠08-eight-08♠','♠09-nine-09♠','♠10-ten-10♠','♠11-jack-11♠','♠12-queen-12♠',
'♠13-king-13♠','♦01-ace-01♦','♦02-two-02♦','♦03-three-03♦','♦04-four-04♦',
'♦05-five-05♦','♦06-six-06♦','♦07-seven-07♦','♦08-eight-08♦','♦09-nine-09♦',
'♦10-ten-10♦','♦11-jack♦-11','♦12-queen-12♦', '♦13-king-13♦','♣01-ace-01♣',
'♣02-two-02♣','♣03-three-03♣','♣04-four-04♣','♣05-five-05♣','♣06-six-06♣',
'♣07-seven-07♣','♣08-eight-08♣','♣09-nine-09♣','♣10-ten-10♣','♣11-jack-11♣',
'♣12-queen-12♣','♣13-king-13♣'

    ]

card = random.choice(deck)

running = True
while running:
        

    print("YOUR CARD = ", card,"\n")

    card_value = int(card[1:3])
    deck.remove(card)

    nextcard = random.choice(deck)
   # print(nextcard)    #For debugging 

    nextcard_value = int(nextcard[1:3])

    inputting = True
    while inputting:
        imp = input("Is the next card Hi, Lo, or Same\n")
       
        if imp == "h" and card_value < nextcard_value or\
           imp == "l" and card_value > nextcard_value or\
           imp == "s" and card_value == nextcard_value:
            print("Correct\n It was a", nextcard,"\n" )
            card = nextcard
            inputting = False
        elif imp == "h" and card_value > nextcard_value or\
             imp == "l" and card_value < nextcard_value or\
             imp == "s" and card_value != nextcard_value:
                 print("Incorrect, It was a ,", nextcard, "Please Play Again")
                 running = False
                 break
        else:
            print("Please Enter a Valid Command, Your Card =,", card) 
            continue


print("~~~Game Over~~~")


