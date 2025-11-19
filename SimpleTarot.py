import sys
import os
import random

# Cards
SUITS = ["Wands", "Cups", "Swords", "Pentacles"]
FACES = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]
MAJOR_ARCANA = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgment", "The World"]    

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def exit():
    sys.exit()

def initializeDeck() -> list:
    deck = list()

    # Add major arcana cards
    for majorArcana in MAJOR_ARCANA:
        deck.append(majorArcana)
    
    # Add minor arcana cards
    for suit in SUITS:
        for face in FACES:
            minorArcanaCard = "The " + face + " of " + suit
            deck.append(minorArcanaCard)
    
    return deck

def dealCards():
    tarotDeck = initializeDeck()
    choice = ''

    clearScreen()
    print("Here is your reading:\n")

    # Get 3 random cards
    spread = random.sample(tarotDeck, 3)
    for card in spread:
        print(card)

    print('')

    while True:
        choice = (input("Would you like to deal a new spread of cards? [yes/no]: "))
        if choice.lower() == 'yes' or choice.lower() == 'y':
            dealCards()
        elif choice.lower() == 'no' or choice.lower() == 'n':
            exit()
        else:
            print("Please type yes or no")

def main():
    choice = ''

    print("Welcome to SimpleTarot!\n")

    while True:
        choice = (input("Would you like to deal a spread of cards? [yes/no]: "))
        if choice.lower() == 'yes' or choice.lower() == 'y':
            dealCards()
        elif choice.lower() == 'no' or choice.lower() == 'n':
            exit()
        else:
            print("Please type yes or no")

main()