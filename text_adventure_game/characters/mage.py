# characters/mage.py

from .character import Character 

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)

    def choose_action(self):
        from .actions import get_random_action #lazy import of the random action
        enemy_action = get_random_action(self) # get a random action from the enemy
        print("\nChoose your action:") #prompt for action choice
        print("1. Attack 1 (Fireball)") #option 1
        print("2. Attack 2 (Lightning Bolt)") #option 2
        print("3. Heal ") #option 3
        print("4. Defend") #option 4
        choice = input("Enter your Action Type (1, 2, 3, or 4): ")

        if choice == '1':
            return "attack1" # return action type
        elif choice == '2':
            return "attack2" # return action type
        elif choice == '3':
            return "heal" # return action type
        elif choice == '4':
            self.defend() #call defend method
            return "defend"
        else:
            print("Invalid choice. Defaulting to Attack 1.") # Handle invalid input
            return "attack1" #default action
        
    def heal(self):
        heal_amount = 20
        self.health += heal_amount
        print(f"{self.name} casts Heal and restores {heal_amount} health points!")
        