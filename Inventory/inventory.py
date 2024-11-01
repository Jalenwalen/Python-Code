# inventory.py

from item import Item

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if isinstance(item, Item):
            self.items[item.item_id] + item
    
    def update_item(self, item_id, amount):
        if item_id in self.items:
            self.items[item_id].update_quantity(amount)
            return True
        return False
    
    def show_inventory(self):
        if not self.items:
            print("The Inventory is Empty.")
        else:
            for item in self.items.values():
                print(item)