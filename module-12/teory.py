


# Singleton
class Config:
    _isinstance = None
    def __new__(cls):
        if cls._isinstance is None:
            cls._isinstance = super().__new__(cls)
            cls._isinstance.mode = 'prod'
        return cls._isinstance

# Factory Method

class EmailSender:
    def send(self, message):
        return f'Email: {message}'
    
class SmsSender:
    def send(self, message):
        return f'SMS: {message}'
    
class NotificationFactory:
    @staticmethod
    def create(channel):
        if channel == 'email':
            return EmailSender()
        elif channel == 'SMS':
            return SmsSender()
        return ValueError('Unknown channel')
    
sender = NotificationFactory.create('SMS')
# print(sender.send('ваше sms'))

# Abstract factory
class LightButton:
    def render(self):
        return 'Light button'

class LightInput:
    def render(self):
        return 'Light input'
    
class DarkButton:
    def render(self):
        return 'Dark button'

class DarkInput:
    def render(self):
        return 'Dark input'
    
class LightTheme:
    def create_button(self):
        return LightButton()
    def create_input(self):
        return LightInput()
    
class DarkTheme:
    def create_button(self):
        return DarkButton()
    def create_input(self):
        return DarkInput()
    
def build_form(factory):
    button = factory.create_button()
    input = factory.create_input()
    print(button.render(), input.render())

# build_form(DarkTheme())

# Builder
class LaptopBuilder:
    def __init__(self):
        self.laptop = {
            'cpu': 'Intel 15',
            'ram': 0,
            'ssd': 256,
            'gru': 'intergrsaded'
        }
    
    def for_study(self):
        self.laptop['ram'] = 16
        self.laptop['ssd'] = 512
        return self
    
    def for_gaming(self):
        self.laptop['ram']= 32
        self.laptop['ssd'] = 1024
        self.laptop['gpu'] = 'RTX 4070'
        return self
    
    def with_cpu(self, cpu):
        self.laptop['cpu'] = cpu
        return self

    def build(self):
        return self.laptop.copy()
    
# print(LaptopBuilder().for_study().with_cpu('Intel 17').build())

# Prototype 
import copy

temp = {
    'delivery': 'standard',
    'promo': False,
    'items': ['book']
}

fast = copy.deepcopy(temp)
fast['delivery'] = 'express'

# Adapter
class OldSmsService:
    def send_sms(self, phone, txt):
        print(f'old service: {phone} : {txt}')

class SmsAdapter:
    def __init__(self, service, phone):
        self.service = service
        self.phone = phone
    def send(self, message):
        self.service.send_sms(self.phone, message)

# SmsAdapter(OldSmsService(), '79603064931').send('sms')

# Bridge

class TV:
    def turn_on(self):
        return 'TV is on'
    
class Radio:
    def turn_on(self):
        return 'Radio is on'
    
class RemoveControl:
    def __init__(self, device):
        self.device = device
    def power(self):
        return self.device.turn_on()
    
# print(RemoveControl(TV()).power())

# Composite

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size
    
class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []
    def add(self, child):
        self.children.append(child)
    
    def get_size(self):
        return sum(child.get_size() for child in self.children)
    
docs = Folder('docs')
docs.add(File('text_1.txt', 10))
docs.add(File('text_2.txt', 20))

# print(docs.get_size())

# Decarator
class Coffee:
    def price(self):
        return 120

    def description(self):
        return 'Кофе'

class MilkDecorator:
    def __init__(self, drink):
        self.drink = drink
    
    def price(self):
        return self.drink.price() + 30
    
    def description(self):
        return self.drink.description + ', Молоко'
    
class SypupDecorator:
    def __init__(self, drink):
        self.drink = drink
    
    def price(self):
        return self.drink.price() + 25
    
    def description(self):
        return self.drink.description + ', сироп'
    
drink = SypupDecorator(MilkDecorator(Coffee()))
# print(drink.price())

# Facade
class PaymentService:
    def pay(self, amount):
        print(f'Оплата {amount} прошла')

class WarehouseService:
    def reserve(self, item):
        print(f'Товар {item} зарезервирован')

class DeliveryService:
    def create(self, item):
        print(f'Доставка для {item} создана')

class OrderFacade:
    def __init__(self):
        self.payment = PaymentService()
        self.warehouse = WarehouseService()
        self.delivery = DeliveryService()

    def place_order(self, item, amount):
        self.payment.pay(amount)
        self.warehouse.reserve(item)
        self.delivery.create(item)

# OrderFacade().place_order('наушники', 300)

# Flyweight

class Flyweight:
    def __init__(self, color):
        self.color = color
    def draw(self, x, y):
        print(self.color, x, y)

class Factory:
    _cached = {}

    @classmethod
    def get(cls, color):
        if color not in cls._cached:
            cls._cached[color] = Flyweight(color)
        return cls._cached[color]
    
red1 = Factory.get('red')
red2 = Factory.get('red')

# print(red1 is red2)

# Proxy

class Image:
    def __init__(self, path):
        print('Загрузка')
        self.path = path
    
    def show(self):
        print(f'Show {self.path}')
    
class ImageProxy:
    def __init__(self, path):
        self.path = path
        self._real = None
    
    def show(self):
        if self._real is None:
            self._real = Image(self.path)
        self._real.show()

# img = Image('photo.png')
# img.show()
# img.show()

# Поведенческие паттерны

# Chain of responsibility

class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler
    
    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return '200 OK'

class AuthHandler(Handler):
    def handle(self, request):
        if not request.get('user'):
            return '401 Error'
        return super().handle(request)
    
class RoleHandler(Handler):
    def handle(self, request):
        if request.get('role') != 'admin':
            return '403 forbidden'
        return super().handle(request)
    
chain = AuthHandler(RoleHandler())

# print(chain.handle({'user': 'alice', 'role': 'admin'}))

# Command
class Light:
    def on(self):
        print('Light is on')

class TurnOnCommand:
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()
    
class Button:
    def __init__(self, command):
        self.command = command

    def press(self):
        self.command.execute()


# Button(TurnOnCommand(Light())).press()

# Mediator

class ChatMediator:
    def send(self, message, user):
        for c in user.collegues:
            if c is not user:
                c.receive(message)

class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        self.collegues = []

    def send(self, message):
        self.mediator.send(f'{self.name}: {message}', self)

    def receive(self, message):
        print(message)

mediator = ChatMediator()
alice = User('Alice', mediator)
bob = User('Bob', mediator)
alice.collegues = [alice, bob]
bob.collegues = [alice, bob]
# mediator.send('aa', alice)

# Memento
class Editor:
    def __init__(self):
        self.text = ''
    
    def write(self, text):
        self.text += text

    def save(self):
        return self.text
    
    def restore(self, snap):
        self.text = snap

editor = Editor()
editor.write("Hello")
sn = editor.save()
editor.write(', world')
# print(editor.text)
editor.restore(sn)
# print(editor.text)

# Observer

class Order:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, listener):
        self.subscribers.append(listener)
    
    def set_status(self, status):
        for subscriber in self.subscribers:
            subscriber(status)

def email_listener(status):
    print(f'Email: Произошла смена статуса на {status}')

def sms_listener(status):
    print(f'SMS: Произошла смена статуса на {status}')

order = Order()
order.subscribe(email_listener)
order.subscribe(sms_listener)
# order.set_status('delivery')

# state
class DraftState:
    def publish(self, document):
        document.state = ReviewState()
        return 'Черновик отправлен'
    
class ReviewState:
    def publish(self, document):
        document.state = PublishedState()
        return 'Документ опубликован'
    
class PublishedState:
    def publish(self, document):
        return 'Уже опубликовано'
    
class Document:
    def __init__(self):
        self.state = DraftState()

    def publish(self):
        return self.state.publish(self)
    
doc = Document()
print(doc.publish())
print(doc.publish())

print(doc.publish())

