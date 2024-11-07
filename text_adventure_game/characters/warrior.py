# characters/warrior.py

from .character import Character 

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)

    def choose_action(self):
        print("\nChoose your action:")
        print("1. Attack 1 (basic attack)")
        print("2. Attack 2 (powerstrike)")
        print("3. Defend")
        choice = input("Enter action type (1, 2, or 3)")

        if choice == '1':
            return "attack1"
        elif choice == '2':
            return "attack2"
        elif choice == '3':
            return "defend"
        else:
            return "invalid"      