from pokeclone.writing import validate_input, format_choices

GENDERS = ["boy", "girl"]
NATURES = ["kind", "mean", "funny", "brave", "nerdy"]

class Player:
    def __init__(self, name, gender, nature):
        self.name = name
        self.gender = gender
        self.nature = nature
        # self.pokelist = [starter]
        self.money = 100
        self.bag = {}
        self.x = 0
        self.y = 0

    def pos():
        return [x, y]

def initialize_player():
    name = input("Please enter trainer name: ")
    print("Are you a boy?\nOr a girl?")
    gender = validate_input(f"Please enter trainer gender ({format_choices(GENDERS)}): ", GENDERS)
    nature = validate_input(f"Please enter trainer nature ({format_choices(NATURES)}): ", NATURES)
    return Player(name, gender, nature)
