#characters/character.py
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power_ = attack_power
        self.defending = False

    def choose_action(self):
        raise NotImplementedError("This method should be overrided by subclasses")
    
    def attack(self, target, attack_type):
        if attack_type == "attack1":
            damage = self.attack_power
            print(f"{self.name} uses Attack 1!")
        elif attack_type == "attack2":
            damage = self.attack_power + 5 
            print(f"{self.name} uses Attack 2!")
        elif attack_type == "heal":
            damage = 0
            print(f"{self.name} attempts to heal!") 
        else:
            damage = self.attack_power
            print(f"{self.name} uses a basic attack!")

        # check if target is defending
        if target.defending:
            print(f"{target.name} defended the attack!")
            damage = 0
            target.defending = False
        
        target.health -= damage 
        print(f"{self.name} attacks {target.name} for {damage} damage")

    def defend(self):
        self.defending = True
        print(f"{self.name} is defending against the next attack!")

    def is_alive(self):
        return self.health > 0
    
    def __str__(self):
        return f"{self.name}: Health = {self.health}, Attack Power = {self.attack_power}"

               