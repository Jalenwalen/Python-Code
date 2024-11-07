# characters/mage.py

from .character import Character 

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)


    def choose_action(self):
        from .actions import get_random_action
        enemy_action = get_random_action(self)
        print("\nChoose your action:")
        print("1. Attack 1 (Fireball)")
        print("2. Attack 2 (Lightning Bolt)")
        print("3. Heal ")
        print("4. Defend")
        choice = input("Enter your choice: ")

        if choice == '1':
            return "attack1"
        elif choice == '2':
            return "attack2"
        elif choice == '3':
            return "defend"
        else:
            return "invalid"   