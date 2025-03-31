#Kids Game
class Frog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f"{self} the Frog encounters {obstacle} and {act}!"
        print(msg)

class Bug:
    def __str__(self):
        return "a bug"
    def action(self):
        return "eats it"
    
# Abstract Factory for Frog game. 
# Advantage is if we change the game characters still the factory functions won't change and thus the environment who uses it.
class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    def __str__(self):
        return "\n\n\t------ Frog World -------"
    def make_character(self):
        return Frog(self.player_name)
    def make_obstacle(self):
        return Bug()
    

# Adult Game
class Wizard:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f"{self} the Wizard battles against {obstacle} and {act}!"
        print(msg)

class Ork:
    def __str__(self):
        return "an evil ork"
    def action(self):
        return "kills it"
    

#abstract Factory class for creating Wizrd characters
class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    def __str__(self):
        return "\n\n\t------ Wizard World -------"
    def make_character(self):
        return Wizard(self.player_name)
    def make_obstacle(self):
        return Ork()
    
# Game environment now
class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()
    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    age = None
    try:
        age_input = input(
            f"Welcome {name}. How old are you? "
        )
        age = int(age_input)
    except ValueError:
        print(
            f"Age {age} is invalid, please try again..."
        )
        return False, age
    return True, age


#finally using it in main
def main():

    name = input("Hello, Whats your name ?")

    valid_input = False

    while not valid_input:
        valid_input, age = validate_age(name)
    
    game = FrogWorld(name) if age<18 else WizardWorld(name)
    
    print(type(game))

    environment = GameEnvironment(game)
    environment.play()

if __name__ == "__main__":
    main()