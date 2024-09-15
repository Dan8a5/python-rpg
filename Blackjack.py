# Import the random module to use for shuffling cards
import random

# Define a dictionary for ASCII art representations of card suits
SUITS = {
    'Hearts': '♥',
    'Diamonds': '♦',
    'Clubs': '♣',
    'Spades': '♠'
}

# Define a multi-line string for the ASCII art of a card template
CARD_TEMPLATE = """
┌─────────┐
│{}       │
│         │
│    {}   │
│         │
│       {}│
└─────────┘
"""

# Define a multi-line string for the ASCII art of the game title
# The 'r' before the string makes it a raw string, treating backslashes as literal characters
GAME_TITLE = r"""
 _____  _____   _____    _____  _            _    _            _    
|  __ \|  __ \ / ____|  |  _ \| |          | |  (_)          | |   
| |__) | |__) | |  __   | |_) | | __ _  ___| | ___  __ _  ___| | __
|  _  /|  ___/| | |_ |  |  _ <| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| | \ \| |    | |__| |  | |_) | | (_| | (__|   <| | (_| | (__|   < 
|_|  \_\_|     \_____|  |____/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                                              _/ |                
                                             |__/                 
"""

# Define a class to represent a single playing card
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # Define how a card should be represented as a string
    def __str__(self):
        return f"{self.value} of {self.suit}"

    # Method to get the ASCII art representation of the card
    def get_ascii_art(self):
        return CARD_TEMPLATE.format(self.value.ljust(2), SUITS[self.suit], self.value.rjust(2))

# Define a class to represent a deck of cards
class Deck:
    def __init__(self):
        # List all possible suits and values
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # Create a list of Card objects for each combination of suit and value
        self.cards = [Card(suit, value) for suit in suits for value in values]
        # Shuffle the deck
        random.shuffle(self.cards)

    # Method to draw a card from the deck
    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

# Define a base class for characters in the game (both player and dealer)
class Character:
    def __init__(self, name):
        self.name = name
        self.hand = []  # List to hold the character's cards

    # Method to draw a card and add it to the character's hand
    def draw(self, deck):
        card = deck.draw()
        if card:
            self.hand.append(card)
        return card

    # Method to calculate the total value of the hand
    def calculate_hand_value(self):
        value = 0
        aces = 0
        for card in self.hand:
            if card.value in ['J', 'Q', 'K']:
                value += 10
            elif card.value == 'A':
                aces += 1
            else:
                value += int(card.value)
        
        # Handle aces
        for _ in range(aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        
        return value

    # Method to display the character's hand, with an option to hide the first card
    def show_hand(self, hide_first=False):
        if hide_first:
            return [self.hand[0].get_ascii_art()] + ['[HIDDEN]'] + [card.get_ascii_art() for card in self.hand[2:]]
        else:
            return [card.get_ascii_art() for card in self.hand]

    # Method to clear the character's hand
    def clear_hand(self):
        self.hand = []

# Define a class for the dealer, inheriting from Character
class Dealer(Character):
    def __init__(self):
        super().__init__("Dealer")

    # Method to play the dealer's turn
    def play(self, deck):
        while self.calculate_hand_value() < 17:
            self.draw(deck)

# Define a class for the player, inheriting from Character
class Player(Character):
    def __init__(self, name, gold):
        super().__init__(name)
        self.gold = gold

    # Method for the player to place a bet
    def place_bet(self, amount):
        if amount <= self.gold:
            self.gold -= amount
            return amount
        else:
            return 0

# Function to display the hands of the player and dealer
def display_hands(player, dealer, hide_dealer=True):
    print(f"\n{player.name}'s hand:")
    for card_art in player.show_hand():
        print(card_art)
    print(f"Hand value: {player.calculate_hand_value()}")

    print(f"\nDealer's hand:")
    for card_art in dealer.show_hand(hide_first=hide_dealer):
        print(card_art)
    if not hide_dealer:
        print(f"Hand value: {dealer.calculate_hand_value()}")

# Function to play a single round of the game
def play_round(dealer, player, deck):
    print(f"\n{player.name}'s Gold: {player.gold}")
    bet = int(input("Place your bet: "))
    actual_bet = player.place_bet(bet)
    
    if actual_bet == 0:
        print("Not enough gold to place that bet.")
        return

    # Clear hands before starting a new round
    player.clear_hand()
    dealer.clear_hand()

    # Initial deal
    for _ in range(2):
        player.draw(deck)
        dealer.draw(deck)

    # Show hands
    display_hands(player, dealer)

    # Player's turn
    while True:
        action = input("Do you want to (H)it or (S)tand? ").lower()
        if action == 'h':
            card = player.draw(deck)
            print(f"You drew:")
            print(card.get_ascii_art())
            display_hands(player, dealer)
            if player.calculate_hand_value() > 21:
                print(f"{player.name} busts!")
                return
        elif action == 's':
            break

    # Dealer's turn
    dealer.play(deck)
    display_hands(player, dealer, hide_dealer=False)

    # Determine winner
    player_value = player.calculate_hand_value()
    dealer_value = dealer.calculate_hand_value()

    if dealer_value > 21:
        print("Dealer busts! You win!")
        player.gold += actual_bet * 2
    elif player_value > dealer_value:
        print(f"{player.name} wins!")
        player.gold += actual_bet * 2
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")
        player.gold += actual_bet

    print(f"{player.name}'s Gold: {player.gold}")

# Main function to run the game
def main():
    print(GAME_TITLE)
    
    # Welcome message
    print("Welcome to RPG Blackjack!")
    print("Try to beat the dealer by getting as close to 21 as possible without going over.")
    print("You start with 1000 gold. Good luck!\n")
    
    # Initialize the game
    deck = Deck()
    dealer = Dealer()
    player = Player("Player", 1000)

    # Main game loop
    while True:
        if len(deck.cards) < 20:
            print("Reshuffling deck...")
            deck = Deck()

        play_round(dealer, player, deck)

        if player.gold <= 0:
            print(f"Game over! {player.name} has run out of gold.")
            break

        play_again = input("Do you want to play another round? (Y/N) ").lower()
        if play_again != 'y':
            break

    print(f"Final Gold: {player.gold}")

# This is the entry point of the script
if __name__ == "__main__":
    main()