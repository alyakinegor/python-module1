from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Ingredient:
    name: str
    key: str
    price: float
    cost: float

@dataclass
class Recipe:
    name: str
    ingridient_keys: list[str]

class RecipeFactory:
    def get_standard_recipes() -> dict[int, Recipe]:
        return {
            0: Recipe('Пицца-1', ['dough', 'cheese', 'tomate', 'mayonaise', 'chiken']),
            1: Recipe('Пицца-2', ['dough','cheese', 'tomate', 'ketchup', 'chiken']),
            2: Recipe('Пицца-3', ['dough','cheese', 'tomate','chiken'])


        }


class PizzaBuilder:
    def __init__(self):
        self._ingridients = ['dough','cheese']
    
    def add_ingridient(self, key):
        if key not in self._ingridients:
            self._ingridients.append(key)
        return self
    
    def build(self):
        return Recipe('Своя пицца', self._ingridients)
    
@dataclass
class OrderItem:
    recipe: Recipe
    quantity: int
    def total_price(self, ingridients: dict[int, Ingredient]):
        one_pizza_price = sum(ingridients[key].price for key in self.recipe.ingridient_keys)
        
        return one_pizza_price * self.quantity
    
    def total_cost(self, ingridients: dict[int, Ingredient]):
        one_pizza_cost = sum(ingridients[key].cost for key in self.recipe.ingridient_keys)
        
        return one_pizza_cost * self.quantity
    
@dataclass
class Order:
    payment_type: str
    items: list[OrderItem]
    def total_price(self, ingridients):
        return sum(item.total_price(ingridients) for item in self.items)
    
    def total_cost(self, ingridients):
        return sum(item.total_cost(ingridients) for item in self.items)
    
    def total_profit(self, ingridients):
        return self.total_price(ingridients) - self.total_cost(ingridients)

    def to_text(self, ingridients: dict[str, Ingredient]) -> str:
        lines = ['Информация о заказе: ']
        for item in self.items:
            ingridients_names = [
                ingridients[key].name for key in item.recipe.ingridient_keys
            ]
            lines.append(f'Пицца: {item.recipe.name}')
            lines.append(f'Количество: {item.quantity}')
            lines.append('Состав:')
            for name in ingridients_names:
                lines.append(f'- {name}')
            
            lines.append(f'Цена позиции: {item.total_price(ingridients)} руб')
        
        lines.append(f'Способ оплаты: {self.payment_type}')

        return '\n'.join(lines)
 
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Оплата наличными на сумму {amount} руб"
    
class CardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Оплата картой на сумму {amount} руб"
    
#-------------
class FileOrderSaver:
    def __init__(self, filename: str = 'order.txt'):
        self.filename = filename

    def save(self, order: Order, ingridients: dict[str, Ingredient]):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write(order.to_text(ingridients))
            f.write('\n' + '-' * 50 + '\n')
        
def create_ingridients():
    return {
        'dough': Ingredient('Тесто', 'dough', 70, 30),
        'cheese': Ingredient('Сыр', 'cheese', 80, 20),
        'tomate': Ingredient("Помидор", "tomate", 20, 5),
        'mayonnaise': Ingredient('Майонез', 'mayonnaise', 50, 10),
        'chicken': Ingredient('Курица', 'chicken', 100, 50),
        'ketchup': Ingredient('Кетчуп', 'ketchup', 15, 3)

    }