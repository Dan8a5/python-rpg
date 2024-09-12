import random  # Import the random module to use random chance in the game

# Base Character class that represents both the hero and enemies
class Character:
    def __init__(self, name, health, power, bounty=0):
        """Initialize a character with a name, health, power, and optional bounty."""
        self.name = name  # Name of the character
        self.health = health  # Health points of the character
        self.power = power  # Attack power of the character
        self.coins = 20  # Start each character with 20 coins
        self.bounty = bounty  # Reward given when the character is defeated

    def alive(self):
        """Check if the character is still alive (health > 0)."""
        return self.health > 0

    def attack(self, enemy):
        """Attack an enemy and deal damage equal to the character's power."""
        enemy.receive_damage(self.power)  # Deal damage to the enemy
        print(f"{self.name} does {self.power} damage to the {enemy.name}.")
        if not enemy.alive():  # Check if the enemy is dead after the attack
            print(f"The {enemy.name} is dead.")
            self.coins += enemy.bounty  # Add enemy's bounty to coins if enemy is dead
            print(f"{self.name} receives {enemy.bounty} coins bounty.")

    def receive_damage(self, damage):
        """Reduce the character's health by the given damage amount."""
        self.health -= damage

    def print_status(self):
        """Print the character's current health and power."""
        print(f"{self.name} has {self.health} health and {self.power} power.")

# Hero class, a special type of character with additional features
class Hero(Character):
    def __init__(self, name="Hero"):
        """Initialize the hero with custom health and power values."""
        super().__init__(name, health=20, power=10)  # Hero starts with 20 health and 10 power
        self.inventory = []  # List to store the hero's items

    def attack(self, enemy):
        """Hero's attack has a 20% chance to deal double damage."""
        if random.random() < 0.2:  # 20% chance for a double damage attack
            damage = self.power * 2
            print(f"{self.name} does {damage} damage (Double Damage!) to the {enemy.name}.")
        else:
            damage = self.power
            print(f"{self.name} does {damage} damage to the {enemy.name}.")
        
        enemy.receive_damage(damage)  # Deal the calculated damage to the enemy
        if not enemy.alive():  # Check if the enemy is dead
            print(f"The {enemy.name} is dead.")
            self.coins += enemy.bounty  # Gain coins from enemy bounty
            print(f"{self.name} receives {enemy.bounty} coins bounty.")

    def buy(self, item):
        """Buy an item if the hero has enough coins."""
        if self.coins >= item.cost:  # Check if the hero has enough coins
            self.coins -= item.cost  # Deduct the cost from hero's coins
            print(f"{self.name} bought {item.name} for {item.cost} coins.")
            item.apply(self)  # Apply the effect of the item to the hero
            self.inventory.append(item)  # Add the item to the hero's inventory
        else:
            print(f"{self.name} doesn't have enough coins to buy {item.name}.")

    def use_item(self, item_name):
        """Use an item from the hero's inventory."""
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.use(self)  # Use the item
                self.inventory.remove(item)  # Remove the item from inventory after use
                return
        print(f"{self.name} doesn't have a {item_name} in their inventory.")

    def print_status(self):
        """Print the hero's current health, power, coins, and inventory."""
        super().print_status()
        print(f"{self.name} has {self.coins} coins.")
        print(f"Inventory: {', '.join([item.name for item in self.inventory])}")

# Goblin class, a specific enemy with predefined attributes
class Goblin(Character):
    def __init__(self):
        """Initialize the goblin with custom health, power, and bounty."""
        super().__init__("Goblin", health=18, power=5, bounty=5)

# Shadow class, a specific enemy with unique damage mechanics
class Shadow(Character):
    def __init__(self):
        """Initialize the shadow with custom health, power, and bounty."""
        super().__init__("Shadow", health=1, power=7, bounty=6)

    def receive_damage(self, damage):
        """Shadow has a 90% chance to avoid damage."""
        if random.random() < 0.1:  # 10% chance to take damage
            super().receive_damage(damage)  # Only take damage 10% of the time
        else:
            print(f"The attack passes through {self.name} without effect!")

# Zombie class, a specific enemy that can resurrect multiple times
class Zombie(Character):
    def __init__(self):
        """Initialize the zombie with custom health, power, and bounty."""
        super().__init__("Zombie", health=10, power=3, bounty=4)
        self.resurrections = 3  # Number of times the zombie can resurrect

    def alive(self):
        """Check if the zombie is still alive or can resurrect."""
        return self.resurrections > 0 or self.health > 0

    def receive_damage(self, damage):
        """Reduce zombie's health, with a chance to resurrect if health reaches 0."""
        super().receive_damage(damage)
        if self.health <= 0 and self.resurrections > 0:
            print(f"{self.name} falls, but rises again!")
            self.health = 10  # Reset health
            self.resurrections -= 1
        elif self.health <= 0 and self.resurrections == 0:
            print(f"{self.name} has been permanently defeated!")

# Wizard class, a specific enemy with mana and special spell attacks
class Wizard(Character):
    def __init__(self):
        """Initialize the wizard with custom health, power, and bounty."""
        super().__init__("Wizard", health=15, power=8, bounty=7)
        self.mana = 50  # Wizards have mana to cast spells

    def attack(self, enemy):
        """Wizard attacks using spells if mana is available, otherwise uses regular attack."""
        if self.mana >= 10:
            spell_power = self.power + 5  # Spells deal 5 extra damage
            self.mana -= 10  # Reduce mana by 10 when casting a spell
            enemy.receive_damage(spell_power)
            print(f"{self.name} casts a spell for {spell_power} damage to {enemy.name}.")
        else:
            super().attack(enemy)  # Fall back to regular attack if out of mana

    def print_status(self):
        """Print the wizard's current health, power, and mana."""
        super().print_status()
        print(f"{self.name} has {self.mana} mana.")

# Archer class, a specific enemy that attacks with arrows
class Archer(Character):
    def __init__(self):
        """Initialize the archer with custom health, power, and bounty."""
        super().__init__("Archer", health=18, power=7, bounty=6)
        self.arrows = 10  # Archers have a limited number of arrows

    def attack(self, enemy):
        """Archer attacks using arrows, with a chance for a critical hit."""
        if self.arrows > 0:  # Check if the archer has arrows left
            critical_chance = 0.2  # 20% chance for a critical hit
            if random.random() < critical_chance:
                damage = self.power * 3  # Critical hits deal 3x damage
                print(f"{self.name} fires a critical shot for {damage} damage to {enemy.name}!")
            else:
                damage = self.power
                print(f"{self.name} shoots an arrow for {damage} damage to {enemy.name}.")
            self.arrows -= 1  # Use up one arrow
            enemy.receive_damage(damage)  # Deal the calculated damage to the enemy
        else:
            print(f"{self.name} is out of arrows and can't attack!")

    def print_status(self):
        """Print the archer's current health, power, and remaining arrows."""
        super().print_status()
        print(f"{self.name} has {self.arrows} arrows left.")

# Item class representing something that can be bought and used by the hero
class Item:
    def __init__(self, name, cost):
        """Initialize the item with a name and cost."""
        self.name = name
        self.cost = cost

    def apply(self, character):
        """Apply the item's effect to the character (to be overridden by subclasses)."""
        pass

    def use(self, character):
        """Use the item on the character."""
        self.apply(character)

# Tonic class, a health-restoring item
class Tonic(Item):
    def __init__(self):
        """Initialize the tonic with a cost of 5 coins."""
        super().__init__("Tonic", 5)

    def apply(self, character):
        """Increase the character's health by 2 when the tonic is used."""
        character.health += 2
        print(f"{character.name}'s health increased by 2. Current health: {character.health}")

# Sword class, an item that increases a character's attack power
class Sword(Item):
    def __init__(self):
        """Initialize the sword with a cost of 10 coins."""
        super().__init__("Sword", 10)

    def apply(self, character):
        """Increase the character's power by 2 when the sword is bought."""
        character.power += 2
        print(f"{character.name}'s power increased by 2. Current power: {character.power}")

# Store class for managing item purchases
class Store:
    # List of available items in the store
    items = [Tonic(), Sword()]

    @classmethod
    def do_shopping(cls, hero):
        """Allow the hero to buy items from the store."""
        print(f"\nWelcome to the Store, {hero.name}!")
        print(f"You have {hero.coins} coins.")
        print("\nAvailable items:")
        for i, item in enumerate(cls.items, 1):  # Loop to display available items
            print(f"{i}. {item.name} (Cost: {item.cost} coins)")
        
        while True:
            choice = input("\nEnter the number of the item you want to buy (or 'q' to quit shopping): ")
            if choice.lower() == 'q':
                break
            try:
                item_index = int(choice) - 1  # Get the index of the selected item
                if 0 <= item_index < len(cls.items):  # Validate the choice
                    hero.buy(cls.items[item_index])  # Buy the selected item
                else:
                    print("Invalid item number.")  # Handle invalid item choice
            except ValueError:
                print("Invalid input. Please enter a number or 'q'.")  # Handle invalid input

# Main game function
def main():
    """Main game loop."""
    hero = Hero(input("Enter your hero's name: "))  # Create a hero with a custom name
    enemies = [Goblin(), Shadow(), Zombie(), Wizard(), Archer()]  # List of possible enemies
    
    while hero.alive():  # Continue the game while the hero is alive
        print("\n" + "=" * 40)
        hero.print_status()
        print("\nChoose an action:")
        print("1. Fight an enemy")
        print("2. Go to the store")
        print("3. Use an item")
        print("4. Flee")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            enemy = random.choice(enemies)  # Select a random enemy
            print(f"\nYou encounter a {enemy.name}!")
            while enemy.alive() and hero.alive():  # Continue battle while both are alive
                print("\nBattle options:")
                print("1. Attack")
                print("2. Do nothing")
                print("3. Flee")
                battle_choice = input("Enter your choice (1-3): ")
                
                if battle_choice == "1":
                    hero.attack(enemy)
                elif battle_choice == "2":
                    print(f"{hero.name} does nothing.")
                elif battle_choice == "3":
                    print(f"{hero.name} flees from the battle!")
                    break
                else:
                    print("Invalid choice. The enemy attacks while you're confused!")
                
                if enemy.alive():
                    enemy.attack(hero)
                print()
                hero.print_status()
                enemy.print_status()
            
            if not enemy.alive():
                print(f"You defeated the {enemy.name}!")
        elif choice == "2":
            Store.do_shopping(hero)  # Enter the store
        elif choice == "3":
            item_name = input("Enter the name of the item you want to use: ")
            hero.use_item(item_name)  # Use an item from inventory
        elif choice == "4":
            print(f"{hero.name} flees from the adventure. Game Over!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    
    if not hero.alive():
        print("Game Over! Your hero has been defeated.")

if __name__ == "__main__":
    main()  # Run the main game function when the script is executed