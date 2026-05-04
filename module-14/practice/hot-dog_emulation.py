
from dataclasses import dataclass
from typing import Protocol
@dataclass
class Hotdog:
    ingredients: list[str]
    price: int
toppings = [
            'mayonaise', 'ketchup', 'sweet_onion', 'halapenio','chili'
        ]
base_hotdogs = {
            1: Hotdog(['dough', 'sausage', "ketchup"], 210),
            2: Hotdog(['dough', 'sausage', 'mayonaise'], 220),
            3: Hotdog(['dough', 'sausage', 'halapenio'], 260)
        }
prices = {
    'mayonaise': 30,
    'ketchup': 20,
    'sweet_onion': 50,
    'halapenio': 70,
    'chili': 60,
    'dough': 100,
    'sausage': 90
}
class Storage:
    def __init__(self):
        self.products = {
            'mayonaise': 10,
            'ketchup': 10,
            'sweet_onion': 10,
            'halapenio': 10,
            'chili': 10,
            'sausage': 10,
            'dough': 10,
            'sausage': 10
        }
    def restore_storage(self, ingredients):
        for i in ingredients:
            if self.products[i] == 3:
                print(f'Предупреждение: продукт {i} скоро закончится!')
            if self.products[i] >= 1:
                self.products[i] -= 1
            else:
                raise ValueError(f'Ошибка! Продукта {i} не хватает!')
    def show_goods(self):
        print('Остатки товара:')
        for k in self.products.keys():
            print(f'{k} - {self.products[k]}')
    



class PaymentStrategy(Protocol):
    @staticmethod
    def pay(price):
        ...

class CashPay:
    @staticmethod
    def pay(price):
        print(f'Оплата {price}Р наличными прошла успешно')

class CardPay:
    def pay(price):
        print(f'Оплата {price}Р по карте прошла успешно')

class Saver:
    def __init__(self):
        self.hotdogs = 0
        self.salary = 0

    @staticmethod
    def save(ingr, amount):
        with open('report.txt', 'a', encoding='utf-8') as f:
            f.write(f'\nЗаказ: {ingr}\n Цена: {amount}\n---------------------------')
    
    def show_statistic(self):
        print('Статистика по продажам: ')
        print(f'Хотдогов продано: {self.hotdogs}\nВыручка: {self.salary}')

class OrderBuilder:
    def _calc_discount(amount):
        amount -= 2
        discount = 0

        for i in range(amount):
            discount += 5
        return discount
    def _pay_order(price):
        ch = input('Выберите тип оплаты:\n 1.Карта\n 2.Наличные: ')
        if ch == '1':
            CardPay.pay(price)
        elif ch == '2':
            CashPay.pay(price)

    def build_common_order():
        global_price = 0
        hotdog_list = []
        while True:
            print(base_hotdogs)
            choice = input('Выберите номер хотдога: ')
            hotdog = base_hotdogs[int(choice)]
            hotdog_list.append(hotdog)
            amount = int(input('Укажите количество: '))
            try:
                storage.restore_storage(hotdog.ingredients*amount)
                dsc = 0
                if amount >= 3:
                    dsc = OrderBuilder._calc_discount(amount)
                    print(f'Ваша скидка: {dsc}%')
                global_price += hotdog.price * amount
                global_price = round((global_price / 100) * (100 - dsc), 2)
                print(f'ваш заказ: {hotdog_list}\nцена: {global_price}')
                saver.hotdogs += amount
                saver.salary += global_price
            except ValueError as e:
                print(e)
            
            choice = input("Хотите добавить что то к заказу?(да/нет)")
            if choice == 'нет':
                Saver.save(hotdog_list, global_price)
                break # переход к оплате
        OrderBuilder._pay_order(global_price)
        
        
    def build_custom_order():            
        global_price = 0
        hotdog_list = []
        while True:
            price = 190
            ingr = ['dough', 'sausage']
            obj = {
                1: 'mayonaise',
                2: 'ketchup',
                3: 'sweet_onion',
                4: 'halapenio',
                5: 'chili'}
            print("""
            1.mayonaise
            2.ketchup
            3.sweet_onion
            4.halapenio
            5.chili""")
            ch = list(map(int, input('Какие ингридиенты вы хотите добавить?(введите числа через пробел)').split(' ')))
            for ing in ch:
                ingr.append(obj[ing])
                price += prices[obj[ing]]
            amount = int(input('Укажите количество хотдоггов: '))
            dsc = 0
            if amount >= 3:
                dsc = OrderBuilder._calc_discount(amount)
                print(f'Ваша скидка: {dsc}%')
            try:
                storage.restore_storage(ingr*amount)
                global_price += price * amount
                global_price = round((global_price / 100) * (100 - dsc), 2)
            except ValueError as e:
                print(e)
                price = 0
                ingr = ['dough', 'sausage']
            
            hotdog_list.append(Hotdog(ingr, price))
            
            ch = input(f'Ваш заказ: {Hotdog(ingr, price)}\n Количество: {amount}\n Добавить еще что то к заказу?(да/нет)')
            if ch == 'нет':
                Saver.save(hotdog_list, global_price)
                saver.hotdogs += amount
                saver.salary += global_price
                break
        OrderBuilder._pay_order(global_price)



storage = Storage()
saver = Saver()
def main():
    while True:
        print("""
Главное меню --------------
1.Купить                  -
2.Просмотреть ингридиенты -
3.Посмотреть статистику   -
4.выход                   -
---------------------------""")
        ch = input('Выберите действие: ')
        if ch == '1':
            print('1.Купить готовый хотдог\n 2.Собрать свой')
            ch = input('Выберите действие: ')
            if ch == '1':
                OrderBuilder.build_common_order()
            elif ch == '2':
                OrderBuilder.build_custom_order()
        if ch == '2':
            storage.show_goods()
        if ch == '3':
            saver.show_statistic()
        if ch == '4':
            break


main()
        




