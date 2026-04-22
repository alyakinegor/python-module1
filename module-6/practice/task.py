"""
ЗАДАЧА: Анализ покупок в магазине

Дан список покупок. Каждая покупка содержит:
- user      : имя покупателя (строка)
- items     : список купленных товаров (список строк)
- price     : общая стоимость покупки (целое число)
- timestamp : время покупки (целое число)

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Посчитать общее количество покупок каждого пользователя.

2. Посчитать общую сумму потраченных денег каждым пользователем.

3. Для каждого пользователя:
   - найти множество уникальных товаров, которые он покупал
   - посчитать общее количество купленных товаров (с учётом повторов)

4. Найти товар, который покупали чаще всего
   (если таких несколько — можно вернуть любой).

5. Найти пользователя, который:
   - потратил больше всего денег
   - купил больше всего товаров
   (это могут быть разные пользователи)

6. Для каждого пользователя найти самый большой перерыв
   между его покупками (по timestamp).
"""

purchases = [
    {"user": "Алиса", "items": ["яблоко", "банан"],          "price": 120, "timestamp": 1},
    {"user": "Боб",   "items": ["банан"],                    "price": 50,  "timestamp": 2},
    {"user": "Алиса", "items": ["апельсин", "яблоко"],       "price": 150, "timestamp": 5},
    {"user": "Боб",   "items": ["яблоко", "апельсин"],       "price": 130, "timestamp": 6},
    {"user": "Алиса", "items": ["банан", "банан"],           "price": 70,  "timestamp": 15},
    {"user": "Боб",   "items": ["банан"],                    "price": 40,  "timestamp": 25},
]

def good_summary():
   res = {}
   for el in purchases:
      res.setdefault(el['user'], 0)
      res[el['user']] += len(el['items'])
   return res

def money_summary():
   res = {}
   for el in purchases:
      res.setdefault(el['user'], 0)
      res[el['user']] += el['price']
   return res

def unique_and_general_goods():

   res = {}
   for el in purchases:
      res.setdefault(el['user'], {'unique_goods': set(), 'summary_of_goods': 0})
      res[el["user"]]['unique_goods'].update(el['items'])
      res[el["user"]]['summary_of_goods'] += len(el['items'])
   return res

def frequent_good():
   res = {}
   for el in purchases:
      for good in el['items']:
         res.setdefault(good, 0)
         res[good] += 1
   m = 0
   good = ''
   for key in res.keys():
      if res[key] > m:
         m = res[key]
         good = key
   return good

def find_user():
   res_cost = {}
   res_goods = {}
   person1 = ''
   person2 = ''
   for el in purchases:
      res_cost.setdefault(el['user'], 0)
      res_cost[el['user']] += el['price']

      res_goods.setdefault(el['user'], 0)
      res_goods[el['user']] += len(el['items'])
   m = 0
   for key in res_cost.keys():
      if res_cost[key] > m:
         m = res_cost[key]
         person1 = key
   n = 0
   for key in res_goods.keys():
      if res_goods[key] > n:
         n = res_goods[key]
         person2 = key
   return f'Потратил больше всего денег: {person1}, купил больше всего товаров: {person2}'

def break_before_shopping():
   res = {}
   for i in purchases:
      res.setdefault(i['user'], [])
      res[i["user"]].append(i['timestamp'])
   for el in res.keys():
      arr = res[el]
      a = 0
      for i in range(0, len(arr)-1):
         if (arr[i+1] - arr[i]) > a:
            a = arr[i+1] - arr[i]
      res[el] = a
   return res



print(good_summary())
print('---------------------------')
print(money_summary())
print('---------------------------')
print(unique_and_general_goods())
print('---------------------------')
print(frequent_good())
print('---------------------------')
print(find_user())
print('---------------------------')
print(break_before_shopping())


def buble_sort(arr):
   for i in range(len(arr)):
      for j in range(len(arr)-1):
         if arr[j] > arr[j+1]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
   return arr

print(buble_sort([1,5,3,6,23,1,6]))