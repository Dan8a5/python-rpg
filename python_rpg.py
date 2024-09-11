class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        enemy.health -= self.power
        print(f"{self.__class__.__name__} does {self.power} damage to the {enemy.__class__.__name__}.")
        if not enemy.alive():
            print(f"The {enemy.__class__.__name__} is dead.")

    def print_status(self):
        print(f"{self.__class__.__name__} has {self.health} health and {self.power} power.")

class Hero(Character):
    def __init__(self):
        super().__init__(health=10, power=5)

class Goblin(Character):
    def __init__(self):
        super().__init__(health=6, power=2)

def main():
    hero = Hero()
    goblin = Goblin()

# Look into the following code and how it works

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
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