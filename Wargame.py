#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the p1uter. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

import random

# Two useful variables for creating Cards.
# SUITE = 'H D S C'.split()
# RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
# SUITE = ['H', 'D', 'S', 'C']
# RANKS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
SUITE = ['H', 'D']
RANKS = ['2','3','4','5','Q','K','A']

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
       self.allcards = []

    def create_deck(self):
        self.rank = ''
        for self.rank in RANKS:
            self.eachsuite = ''
            for self.eachsuite in SUITE:
                self.allcards += [(self.eachsuite,self.rank)]

    def __str__(self):
        return "Cards: %s " %(self.allcards)

    def shuffle_deck(self):
         random.shuffle(self.allcards)


    def split_deck(self):
        # return (self.allcards[:26], self.allcards[26:])
        return (self.allcards[:7], self.allcards[7:])

class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
            drawn_card = self.hand.remove_card()
            print("{} has placed: {}".format(self.name,drawn_card))
            print('\n')
            return drawn_card

    def still_has_cards(self):
        """
        Returns True if player still has cards
        """
        return len(self.hand.cards) != 0

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war

c = Deck()
c.create_deck()
c.shuffle_deck()
FirstPcards,SecondPcards = c.split_deck()


p1 = Player("Player1",Hand(FirstPcards))
p2 = Player("Player2",Hand(SecondPcards))

total_rounds = 0

# Let's play
# while p2.still_has_cards() and p1.still_has_cards():
while total_rounds<4:
    total_rounds += 1
    print("It is time for a new round!")
    print("Here are the current standings: ")
    print(p2.name+" count: "+str(len(p2.hand.cards)))
    print(p1.name+" count: "+str(len(p1.hand.cards)))
    print("Both players play a card!")
    print('\n')

        # Cards on Table represented by list
    table_cards = []

        # Play cards
    p1_card = p1.play_card()
    p2_card = p2.play_card()

        # Add to table_cards
    table_cards.append(p1_card)
    table_cards.append(p2_card)

    # Check to see who had higher rank
        # print(RANKS.index(p1_card[1])
        # print(RANKS.index(p2_card[1])

    if RANKS.index(p1_card[1]) <= RANKS.index(p2_card[1]):
                print(p2.name+" has the higher card, adding to hand.")
                p2.hand.add(table_cards)
    else:
                print(p1.name+" has the higher card, adding to hand.")
                p1.hand.add(table_cards)

    print("Here are the current standings: ")
    print(p2.name+" count: "+str(len(p2.hand.cards)))
    print(p1.name+" count: "+str(len(p1.hand.cards)))

print("Great Game, it lasted: "+str(total_rounds))
