def get_random_action(character):
    actions = []
    if isinstance(character, Mage):
        actions = ['attack1', 'attack2', 'heal', 'defend']
    elif isinstance(character, Warrior):
        actions = ['attack1', 'attack2', 'defend']
    return random.choice(actions)