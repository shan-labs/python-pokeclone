from pokeclone.writing import validate_input, format_choices
from random import choice, randrange

GENDERS = ["boy", "girl"]
NATURES = ["kind", "mean", "funny", "nerdy", "rich", "poor"]
NAMES = {
    "boy": ["john"],
    "girl": ["jane"]
}

DIRECTIONS = {
    "U": [-1, 0],
    "R": [0, 1],
    "L": [0, -1],
    "D": [1, 0]
}
DIRECTION_KEYS = sorted(DIRECTIONS.keys())

class Trainer:
    def __init__(self, name, gender, nature, pokelist, money = 100, bag = {}, heading = "R"):
        self.name = name
        self.gender = gender
        self.nature = nature
        self.pokelist = pokelist
        self.money = money
        self.bag = bag
        self.heading = heading

class Player(Trainer):
    def __init__(self, name, gender, nature, starter):
        # TODO: change to have player do a lookup from pokedex based on name
        Trainer.__init__(self, name, gender, nature, [starter])

    def move(self):
        direction = validate_input(f"Choose: direction ({format_choices(DIRECTION_KEYS)}): ", DIRECTION_KEYS)
        self.heading = direction
        return DIRECTIONS[direction]

    def __str__(self):
        display = f"\tName\n\t\t{self.name}\n"
        display += f"\tGender\n\t\t{self.gender}\n"
        display += f"\tNature\n\t\t{self.nature}\n"
        # TODO: utilize pokemon string method once class is ready
        display += f"\tPokemon\n\t\t{self.pokelist}\n"
        display += f"\tMoney\n\t\t${self.money}\n"
        # TODO: utilize item string method once class is ready
        display += f"\tbag\n\t\t{self.bag}\n"
        return display

def initialize_player():
    name = input("Please enter trainer name: ")
    print("Are you a boy?\nOr a girl?")
    gender = validate_input(f"Please enter trainer gender ({format_choices(GENDERS)}): ", GENDERS)
    nature = validate_input(f"Please enter trainer nature ({format_choices(NATURES)}): ", NATURES)
    STARTERS = {
        "fire": "charmander",
        "water": "squirtle",
        "grass": "bulbasaur"
    }
    element = validate_input(f"Please enter trainer nature ({format_choices(STARTERS.keys())}): ", STARTERS.keys())
    return Player(name, gender, nature, STARTERS[element])

class CPU(Trainer):
    def __init__(self, pokelist):
        gender = choice(GENDERS)
        name = choice(NAMES[gender])
        nature = choice(NATURES)
        money = randrange(0, 101, 5)
        if nature == "rich":
            money *= 1000
        elif nature != "poor":
            money *= 100
        # TODO: fill bag randomly with useful items once item class is ready
        # TODO: smartly determine heading to engage in battle
        Trainer.__init__(self, name, gender, nature, [], money)
