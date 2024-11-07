def get_random_action(self):
    import random
    from characters.mage import Mage
    from characters.warrior import Warrior

    actions = []
    if isinstance(self, Mage)