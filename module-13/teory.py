# Model
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int

class CardModel:
    def __init__(self):
        self.products = {
            'apple': Product('Яблоко', 80),
            'banana': Product('Банан', 60),
            'coffee': Product('Кофе', 250)
        }
        self.items = []

    def add_item(self, product_code: str):
        if product_code not in self.products:
            raise ValueError('такого товара нет')
        self.items.append(self.products[product_code])

    def total(self):
        return sum(item.price for item in self.items)
    
    def item_names(self):
        return [item.name for item in self.items]
    
model = CardModel()
model.add_item('apple')
model.add_item('coffee')
# print(model.item_names())
# print(model.total())

# View

class ConsoleCartView:
    @staticmethod
    def render_card(items, total):
        print('Корзина: ')
        if items:
            for i in items:
                print(f'- {i}')
        else:
            print('- пусто')
    
    @staticmethod
    def render_error(msg):
        print(f'- ошибка: {msg}')

# ConsoleCartView.render_card(['Яблоко', 'Кофе'], 330)

# Controller
class CartController:
    def __init__(self, model: CardModel, view: ConsoleCartView):
        self.model = model
        self.view = view

    def add_product(self, product_code):
        try:
            self.model.add_item(product_code)
            self.view.render_card(self.model.item_names(), self.model.total())
        except ValueError as e:
            self.view.render_error(str(e))

controller = CartController(CardModel(), ConsoleCartView())

controller.add_product('banana')
controller.add_product('coffee')
controller.add_product('water')

