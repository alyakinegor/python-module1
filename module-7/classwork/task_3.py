"""
ЗАДАЧА: Анализ корзины интернет-магазина

Даны данные о заказах.

Каждая строка заказа имеет формат:
order_id,клиент,товары,сумма

Где:
- order_id — идентификатор заказа
- клиент   — имя клиента
- товары   — список товаров, разделённых символом "|"
- сумма    — стоимость заказа (целое число)

Заказы:
order1,Алиса,яблоко|банан|банан,120
order2,Боб,банан|груша,80
order3,Алиса,яблоко|апельсин,150
order4,Кира,яблоко|яблоко|яблоко,90
order5,Боб,банан|яблоко,70
order6,Кира,груша,40

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Записать заказы в файл orders.log

2. Прочитать файл orders.txt и загрузить данные.

3. Для каждого клиента:
   - посчитать общую сумму всех заказов
   - определить множество уникальных товаров,
     которые он покупал

4. Найти самый популярный товар
   (по общему количеству покупок).

5. Найти клиента с самой однообразной корзиной:
   - минимальное количество уникальных товаров

6. Найти товары, которые покупали ВСЕ клиенты.

7. Записать результаты анализа в файл orders_report.txt.
"""
import math
orders = ['order1,Алиса,яблоко|банан|банан,120',
'order2,Боб,банан|груша,80',
'order3,Алиса,яблоко|апельсин,150',
'order4,Кира,яблоко|яблоко|яблоко,90',
'order5,Боб,банан|яблоко,70',
'order6,Кира,груша,40']
with open('orders.log', 'w', encoding='utf-8') as file:
   file.write('\n'.join(orders))

orders.clear()

f = open('orders.log', 'r', encoding='utf-8')
a = f.read().split('\n')
for el in a:
   orders.append(el)

clients = {}
most_popular_good = None

goods = {}
for el in orders:
   arr = el.split(',')
   clients.setdefault(arr[1], {'total_sum': 0, 'goods': set()})
   clients[arr[1]]['total_sum'] += int(arr[-1])
   clients[arr[1]]['goods'].update(arr[-2].split('|'))
   #-------------
   for g in arr[-2].split('|'):
      goods.setdefault(g, 0)
      goods[g] += 1

m = 0  
for key in goods.keys():
   if goods[key] > m:
      m = goods[key]
      most_popular_good = key

m = math.inf
user = None
buys = set()
for key in clients.keys():
   if len(clients[key]['goods']) < m:
      m = len(clients[key]['goods'])
      user = key
   #--------------
   if list(clients.keys()).index(key) == 0:
      buys.update(clients[key]['goods'])
   else:
      buys = buys.intersection(clients[key]['goods'])




def write_report():
   r = open('orders_report.log', 'w', encoding='utf-8')
   for el in clients.keys():
      line = el + ': '
      line += 'сумма покупок: ' + str(clients[el]['total_sum']) + ' ' +  'товары: ' + str(clients[el]['goods']) + '\n'
      r.write(line)
   r.write(f'Самый популярный товар: {most_popular_good}\n')
   r.write(f'Клиент с самой однообразной корзиной: {user}\n')
   r.write(f'Товары, которые купили все: {buys}\n')

write_report()
