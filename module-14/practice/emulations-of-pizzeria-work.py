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
            1: Recipe('Пицца-1', ['dough', 'cheese', 'tomate', 'mayonaise', 'chicken']),
            2: Recipe('Пицца-2', ['dough','cheese', 'tomate', 'ketchup', 'chicken']),
            3: Recipe('Пицца-3', ['dough','cheese', 'tomate','chicken'])


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
        'mayonaise': Ingredient('Майонез', 'mayonaise', 50, 10),
        'chicken': Ingredient('Курица', 'chicken', 100, 50),
        'ketchup': Ingredient('Кетчуп', 'ketchup', 15, 3)

    }

def create_stock():
    return {
        'dough': 10,
        'cheese': 10,
        'tomate': 10,
        'mayonaise': 10,
        'chicken': 10,
        'ketchup': 10,

    }
def get_topping():
    return ['tomate',
        'mayonaise',
        'chicken',
        'ketchup']

def create_custom_recipe(inventory):
    builder = PizzaBuilder()
    print('Создание своей пиццы')
    for key in get_topping():
        ingridient = inventory.ingridients[key]
        choice = input(f'Хотите добавить {ingridient.name}?')
        if choice == 'да':
            builder.add_ingridient(ingridient.key)
    return builder.build()
class Inventory:
    def __init__(self, ingridients, stock):
        self.ingridients = ingridients
        self.stock = stock

    def has_enough(self, ingrident_keys, quantity):
        for key in ingrident_keys:
            if self.stock.get(key, 0) < quantity:
                return False
            return True
        
    def reduce_stock(self, ingridient_keys, quantity):
        for key in ingridient_keys:
            self.stock[key] -= quantity
        
    def show(self):
        print('Наличие ингридиентов')
        for key, count in self.stock.items():
            ingridient = self.ingridients[key]
            print(f'{ingridient.name}: {count}')

class SalesReport:
    def __init__(self):
        self.profit = 0
        self.revenue = 0
        self.sold_count = 0

    def add_order(self, order, ingridients):
        self.sold_count += sum(item.quantity for item in order.items)
        self.revenue += order.total_price(ingridients)
        self.profit += order.total_profit(ingridients)
    
    def show(self):
        print('Отчет')
        print(f'Продано пицц: {self.sold_count}')
        print(f'Выручка: {self.profit}')
        print(f'Доход {self.revenue}')

def show_menu():
    print('1. Создать заказ')
    print('2. Отчет')
    print('3. Наличие ингридиентов')
    print('4. Выход')


def show_standard_recipes(recipes, ingridients):
    print('Стандартные пиццы')
    for number, recipe in recipes.items():
        print(f'{number}. {recipe.name}')
    
    price = sum(ingridients[key].price for key in recipe.ingridient_keys)
    print(f'Цена за штуку: {price}')

def choose_recipe(
        recipes,
        ingridients,
        inventory
    ):
    while True:
        choice = input('Выберите вариант: ')
        if choice == '0':
            return create_custom_recipe(inventory)
        else:
            return recipes[int(choice)]

def choose_payment():
    print('Выберите способ оплаты:')
    print('1 - Наличные')
    print('2 - Карта')
    while True:
        choice = input('Выберите: ')
        if choice == '1':
            return CashPayment(), 'наличные'
        elif choice == '2':
            return CardPayment(), 'Карта'
def create_order(
        ingridients: dict[str, Ingredient],
        inventory: Inventory,
        report: SalesReport,
        file_saver: FileOrderSaver
    ):
    recipes = RecipeFactory.get_standard_recipes()
    items = []
    while True:
        show_standard_recipes(recipes, ingridients)
        recipe = choose_recipe(recipes, ingridients, inventory)
        quantity = int(input('Введите количество: '))
        if not inventory.has_enough(recipe.ingridient_keys, quantity):
            print('Недостаточно ингридиентов для заказа')
            return
        items.append(OrderItem(recipe,quantity))
        more = input('Добавить еще один вид пиццы?')
        if more == 'нет':
            break
    
    payment_strategy, payment_type = choose_payment()

    order = Order(items=items, payment_type=payment_type)

    for item in items:
        inventory.reduce_stock(item.recipe.ingridient_keys, item.quantity)
    
    amount = order.total_price(ingridients)
    print(payment_strategy.pay(amount))
    file_saver.save(order, ingridients)
    report.add_order(order, ingridients)
    
def main():
    ingridients = create_ingridients()
    stock = create_stock()
    inventory = Inventory(ingridients, stock)
    report = SalesReport()
    saver = FileOrderSaver('report.txt')
    while True:
        show_menu()
        choice = input('Выберите пункт меню')
        if choice == '1':
            create_order(ingridients, inventory, report, saver)
        elif choice == '2':
            report.show()
        elif choice == '3':
            inventory.show()
        elif choice == '4':
            break
main()