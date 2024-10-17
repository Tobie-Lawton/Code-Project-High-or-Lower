import random

class Card:

    #Represents a playing card with a suit and rank.
    suits = ["♠", "♥", "♦", "♣"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, rank):

        if not (suit in Card.suits and rank in Card.ranks):
            raise ValueError("Invalid card: " + str(suit) + " " + str(rank))

        self.suit = suit
        self.rank = rank

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

    def deal(self, num_cards = 1):
        pass
          
    def startgame(self,cards):
        play=input("do you waht to play").lower()
        if play == "yes":
            random.shuffle(self.cards)
            oldcard = self.cards.pop(0)
            print(oldcard)
            Desition=input("higher or lower").lower()
            if Desition == "higher":
                newcard = self.cards.pop(0)
                print(newcard)
                if higher(newcard, oldcard):
                    print("words")
            elif Desition == "lower":
                print(self.cards[0])
            else:
                Desition=input("higher or lower").lower()
        elif play == "no":
             print("end program")
        else:
            play=input("do you waht to play").lower()

def card1(self, newcard):
    return Card.rank_value[newcard]

def card2(self, oldcard):
    return Card.rank_value[oldcard]

# true if card1 > card2
def higher(card1, card2):
    True if card1 > card2 else False
    True if card2 < card1 else False
    
def lower(card1, card2):
    True if card1 < card2 else False
    True if card2 > card1 else False    

Deck().startgame(())
