# character class definition 
class Character:
    def __init__(self, health, power): # constructor method
        self.health = health # health assigs the health value to the character
        self.power = power # assisgns the power value, representing how much damage a character can deal 

    def alive(self): # checks if the character  is alive by looking at their health, if health is greater than 0 it returns true; otherwise false
        return self.health > 0

    def attack(self, enemy): # attack method, allows one character to attack the other
        enemy.health -= self.power # reduces the enemy's health by the attackers power
        print(f"{self.__class__.__name__} does {self.power} damage to the {enemy.__class__.__name__}.") #
        if not enemy.alive():
            print(f"The {enemy.__class__.__name__} is dead.") #After the attack, it checks if the enemy is still alive. If not, it prints that the enemy is dead.


    def print_status(self): #This prints the character’s current health and power to the screen.
        print(f"{self.__class__.__name__} has {self.health} health and {self.power} power.")

class Hero(Character): #This defines a specific type of Character called Hero. It inherits from the Character class using class Hero(Character).
    def __init__(self):  #The __init__ method calls super().__init__(...), which invokes the constructor of the parent Character class, giving the hero 10 health and 5 power.
        super().__init__(health=20, power=10)

class Goblin(Character): #Similar to Hero, the Goblin class inherits from Character.
    def __init__(self):
        super().__init__(health=18, power=5)#A goblin has 6 health and 2 power, set by calling super().__init__.

def main(): #The main function is where the game starts.
    hero = Hero() #It creates two objects: hero and goblin, each with their predefined health and power.
    goblin = Goblin()



    while goblin.alive() and hero.alive(): #This while loop keeps running as long as both the hero and the goblin are alive.
        hero.print_status() #Inside the loop, it prints the status (health and power) of both the hero and the goblin.
        goblin.print_status()
        print() #the player has three choices, the players input is stored in the variable user_input
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end="")
        user_input = input()

        if user_input == "1":
            hero.attack(goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {user_input}")

        if goblin.alive():
            goblin.attack(hero)

        if not hero.alive():
            print("You are dead.")

if __name__ == "__main__":
    main()