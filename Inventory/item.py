# Item.py
class Item:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount):
        self.quantity += amount
    
    def __str__(self):
        return f"{self.name} (ID: {self.item_id}): {self.quantity} in stock, ${self.price} each"
    