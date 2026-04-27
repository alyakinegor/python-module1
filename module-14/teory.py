# S - single responsibility

# Плохой пример
class BadReport:
    def __init__(self, title, rows):
        self.title = title
        self.rows = rows

    def as_text(self):
        lines = [self.title, '-' * len(self.rows)]
        for row in self.rows:
            lines.append(f"{row['name']}: {row['value']}")
        return '\n'.join(lines)
    
    def save(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.as_text())
    
# Хороший пример
from dataclasses import dataclass

@dataclass
class Report:
    title: str
    rows: list[str]

class TextReportFormatter:
    def format(self, report):
        lines = [report.title, '-' * len(report.rows)]
        for row in report.rows:
            lines.append(f"{row['name']}: {row['value']}")
        return '\n'.join(lines)
    
class FileStorage:
    def save(self, filename, content):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

rep = Report('title', [{'name': 'books', 'value': 100}])
# print(TextReportFormatter().format(rep))

# O - Open/Closed

# Плохой пример
def calculate_discount(customer_type, amount):
    if customer_type == 'regular':
        return amount * 0.05
    if customer_type == 'vip':
        return amount * 0.15
    if customer_type == 'customer':
        return amount * 0.30
    return 0

# print(calculate_discount('regular', 10000))

#  Хороший пример
from typing import Protocol

class Discount(Protocol):
    def discount_for(self, amount):
        ...

class RegularDiscount:
    def discount_for(self, amount):
        return amount * 0.05

class VipDiscount:
    def discount_for(self, amount):
        return amount * 0.15
    
class CustomerDiscount:
    def discount_for(self, amount):
        return amount * 0.30
    
class NoDiscount:
    def discount_for(self, amount):
        return 0
    
def final_price(amount, discount: Discount):
    return amount - discount.discount_for(amount)

# L - Liskow Substitution

# Плохой пример
# class BadBird:
#     def fly(self):
#         print('Летит')

# class BadSparrow(BadBird):
#     pass

# class BadPinguin(BadBird):
#     def fly(self):
#         raise ValueError('Пингвины не летают')
    
# def make_bird_fly(bird: BadBird):
#     bird.fly()

# make_bird_fly(BadSparrow())

# try:
#     make_bird_fly(BadPinguin())
# except ValueError as e:
#     print("Ошибка: ", e)

# Хороший пример
from dataclasses import dataclass

@dataclass
class Bird:
    name: str

class Flyable(Protocol):
    def fly(self) -> None:
        ...

class Sparrow(Bird):
    def fly(self):
        print(f'{self.name} летит')

class Pinguin(Bird):
    def swim(self):
        print(f'{self.name} плывет')

def make_fly(obj: Flyable):
    obj.fly()

# make_fly(Sparrow('Воробей'))

# Pinguin('Пингвин').swim()

# I - Interface Segregation
# Плохой пример
from abc import ABC, abstractmethod

class BadDeviceOffice(ABC):
    @abstractmethod
    def print_document(self, text):
        pass

    @abstractmethod
    def scan_document(self):
        pass

    @abstractmethod
    def send_fax(self, phone, text):
        pass

class Printer(BadDeviceOffice):
    def print_document(self, text):
        print('Печать: ', text)
    
    def scan_document(self):
        raise NotImplementedError('Принтер не сканирует')
    
    def send_fax(self, phone, text):
        raise NotImplementedError('Принтер не отправляет fax')
    
# Хороший пример

from typing import Protocol

class Printer(Protocol):
    def print_document(self, text):
        ...

class Scanner(Protocol):
    def scan_document(self, text):
        ...

class LPrinter:
    def print_document(self, text):
        print('Печать документа')

class MFPrinter:
    def print_document(self, text):
        print('Печать документа')
    
    def scan_document(self, text):
        print('Скан выполнен')

def print_document(device: Printer):
    device.print_document("Документ")

def scan_document(device: Scanner):
    device.scan_document('scan')

print_document(LPrinter())
print_document(MFPrinter())
scan_document(MFPrinter())

# D - Dependency Inversion

# Плохой пример 
class EmailSender:
    def send(self, email, message):
        print(f'Email для {email}:{message}')

class OrderService:
    def __init__(self):
        self.sender = EmailSender()

    def complete_order(self, email, total):
        print(f'Заказ на сумму {total} оформлен')
        self.sender.send(email, 'Ваш заказ оформлен')

OrderService().complete_order('user@example.com', 3500)

# Хороший пример
from typing import Protocol

class Notifier(Protocol):
    def send(self, contact, message):
        ...

class EmailNotifier:
    def send(self, contact, message):
        print(f'Email для {contact}:{message}')

class SMSNotifier:
    def send(self, contact, message):
        print(f'sms для {contact}:{message}')

class OrderService:
    def __init__(self, notifier: Notifier):
        self.sender = notifier

    def complete_order(self, message, total):
        print(f'Заказ на сумму {total} оформлен')
        self.sender.send(message, 'Ваш заказ оформлен')

OrderService(EmailNotifier()).complete_order('user@example.com', 3500)
OrderService(SMSNotifier()).complete_order('+799999999', 3500)
