from IPython.core.display import clear_output
import random

class Card:

    #Represents a playing card with a suit and rank.
    suits = ["♥","♣","♦","♠",]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, rank):

        if not (suit in Card.suits and rank in Card.ranks):
            raise ValueError("Invalid card: " + str(suit) + " " + str(rank))

        self.suit = suit
        self.rank = rank
        #self.value = (Card.index(suit))*(Card.index(rank))
        self.value = self.ranks.index(rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def card_str(self):
        if self.rank == "10":
            return f"""
            ┌─────┐
            │10   │
            │  {self.suit}  │
            │   10│
            └─────┘
            """
        else:
            return f"""
            ┌─────┐
            │{self.rank}    │
            │  {self.suit}  │
            │    {self.rank}│
            └─────┘
            """

class Deck:

    #Initializes a Deck object with a full deck of 52 cards.
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        
    
    def shuffle(self):
        random.shuffle(self.cards)

    def debug_print_deck(self):
        for card in self.cards:
            print(card.card_str())
    
    def startgame(self):
        play=input("Do You What To Play ").lower()
        if play == "yes":
            hi = True
            random.shuffle(self.cards)
            oldcard = self.cards.pop(0)
            print(oldcard)
            hi = True
        elif play == "no":
            print("Good Bye")
            hi = False
        else:
            play=input("Do You What To Play ").lower()
    
        while hi == True:
            Desition=input("Higher Or Lower ").lower()
            if Desition == "higher":
                newcard = self.cards.pop(0)
                if higher(oldcard, newcard) == True:
                    print("Corrent")
                    print(newcard)
                elif higher(oldcard, newcard) == False:
                    print ("You Lose")
                    hi = False
            elif Desition == "lower":
                newcard = self.cards.pop(0)
                if lower(oldcard, newcard) == True:
                    print("Corrent")
                    print(newcard)
                elif lower(oldcard, newcard) == False:  
                    print ("You Lose")
                    hi = False
            else:
                Desition=input("Ither Enter Higher Or Lower ").lower()
                
def higher(oldcard, newcard):
    return newcard.value > oldcard.value

def lower(newcard, oldcard):
    return newcard.value < oldcard.value   

deck_instance = Deck()
deck_instance.startgame()
