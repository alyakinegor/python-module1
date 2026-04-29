from dataclasses import dataclass

@dataclass
class Hotdog:
    ingredients: list[str]
    price: int
toppings = [
            'mayonaise', 'ketchup', 'sweet_onion', 'halapenio','chili'
        ]
base_hotdogs = {
            1: Hotdog(['dough', 'sausage', "ketchup"], 200),
            2: Hotdog(['dough', 'sausage', 'mayonaise'], 200),
            3: Hotdog(['dough', 'sausage', 'halapenio'], 200)
        }

class Storage:
    def __init__(self):
        self.products = {
            'mayonaise': 10,
            'ketchup': 10,
            'sweet_onion': 10,
            'halapenio': 10,
            'chili': 10
        }
    def restore_storage(self, ingredients):
        for i in ingredients:
            if self.products >= 1:
                self.products[i] -= 1
            else:
                print(f'Продукта {i} не хватает!')

class OrderBuilder:
    def build_common_order():
        pass
    def build_custom_order(ingredients):
        pass


