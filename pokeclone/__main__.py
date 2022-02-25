from pokeclone.archetypes import characters

if __name__ == '__main__':
    print("Welcome to PokeClone!")
    name = input("Please enter trainer name:")
    gender = input("Please enter trainer gender:")
    nature = input("Please enter trainer nature:")
    p = characters.Player(name, gender, nature)
    print(p)
