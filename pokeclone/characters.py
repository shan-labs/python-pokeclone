from pokeclone.writing import validate_input, format_choices

GENDERS = ["boy", "girl"]
NATURES = ["kind", "mean", "funny", "brave", "nerdy"]

DIRECTIONS = {
    "U": [-1, 0],
    "R": [0, 1],
    "L": [0, -1],
    "D": [1, 0]
}
DIRECTION_KEYS = sorted(DIRECTIONS.keys())

class Player:
    def __init__(self, name, gender, nature):
        self.name = name
        self.gender = gender
        self.nature = nature
        # self.pokelist = [starter]
        self.money = 100
        self.bag = {}

    def move(self):
        direction = validate_input(f"Choose: direction ({format_choices(DIRECTION_KEYS)}): ", DIRECTION_KEYS)
        return direction, DIRECTIONS[direction]

def initialize_player():
    name = input("Please enter trainer name: ")
    print("Are you a boy?\nOr a girl?")
    gender = validate_input(f"Please enter trainer gender ({format_choices(GENDERS)}): ", GENDERS)
    nature = validate_input(f"Please enter trainer nature ({format_choices(NATURES)}): ", NATURES)
    return Player(name, gender, nature)
