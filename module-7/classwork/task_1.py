"""
ЗАДАЧА: Учёт инвентаря на складе

Формат строки:
дата,товар,тип,количество

Операции:
2024-01-01,яблоко,IN,50
2024-01-02,банан,IN,30
2024-01-03,яблоко,OUT,10
2024-01-03,груша,OUT,5
2024-01-04,груша,IN,20
2024-01-05,банан,OUT,40
2024-01-06,яблоко,OUT,5

Типы операций:
- IN  : поступление товара
- OUT : отгрузка товара

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Создать файл inventory.txt с операциями склада

2. Прочитать файл и загрузить все операции.

3. Для каждого товара:
   - посчитать итоговое количество на складе
   - посчитать общее количество поступивших единиц
   - посчитать общее количество отгруженных единиц

4. Найти товары:
   - у которых итоговое количество < 0 (ошибка учёта)
   - которые ни разу не поступали, но отгружались

5. Найти товар с:
   - максимальным количеством поступлений
   - максимальным количеством отгрузок

6. Сформировать множество всех дат,
   когда происходили операции с товаром "яблоко".

7. Записать подробный отчёт в файл report.txt.

- ОТЧЁТ ПО СКЛАДУ
- Итоговые остатки
- Общее поступление
- Общая отгрузка
- Товары с отрицательным остатком:
- Товары без поступлений, но с отгрузкой:
- Товар с максимальным поступлением:
- Товар с максимальной отгрузкой:
- Даты операций с яблоком:
"""
logs = ['2024-01-01,яблоко,IN,50', '2024-01-02,банан,IN,30', '2024-01-03,яблоко,OUT,10', 
        '2024-01-03,груша,OUT,5', '2024-01-04,груша,IN,20','2024-01-05,банан,OUT,40','2024-01-06,яблоко,OUT,5']

with open('inventory.txt', 'w+', encoding='utf-8') as f:
   for el in logs:
      f.write(f'{el}\n')
   f.write('2024-09-07,мандарин,OUT,5')

a = ""
f = open('inventory.txt', 'r', encoding='utf-8')
a = f.read().split('\n')
def total_quantity():
   res = {}

   for line in a:
      arr = line.split(',')
      res.setdefault(arr[1], 0)
      if arr[-2] == 'IN':
         res[arr[1]] += int(arr[-1])
      else:
         res[arr[1]] -= int(arr[-1])
      
   return res

def total_in():
   res = 0
   for line in a:
      if line.split(',')[-2] == 'IN':
         res += int(line.split(',')[-1])
   return res

def total_out():
   res = 0
   for line in a:
      if line.split(',')[-2] == 'OUT':
         res += int(line.split(',')[-1])
   return res


def f4_1():
   res = total_quantity()
   arr = []
   for k in res.keys():
      if res[k] < 0:
         arr.append(k)
   return arr

def f4_2():
   set_in = set()
   set_out = set()
   for line in a:
      arr = line.split(',')
      if 'IN' in arr:
         set_in.add(arr[1])
      else:
         set_out.add(arr[1])
   return set_out.difference(set_in)

def f5_1():
   res_in = {}
   res_out = {}
   ans1 = 0
   ans2 = 0
   for line in a:
      arr = line.split(',')
      res_in.setdefault(arr[1], 0)
      res_out.setdefault(arr[1], 0)
      if 'IN' in arr:
         res_in[arr[1]] += 1
      else:
         res_out[arr[1]] += 1
   for k in res_in.keys():
      if res_in[k] > ans1:
         ans1 = res_in[k]
   for k in res_out.keys():
      if res_out[k] > ans2:
         ans2 = res_out[k]
   return f'максимальное количество поступлений: {ans1}, максимальное количество отгрузок: {ans2}'

def f6():
   apple_set = set()
   for line in a:
      arr = line.split(',')
      if 'яблоко' in arr:
         apple_set.add(arr[0])
   return apple_set


print(str(total_quantity()))
r = open('report.txt', 'w', encoding='utf-8')

r.write('Итоговые остатки:\n')
r.write(str(total_quantity()))
r.write('\nОбщее поступление:\n')
r.write(str(total_in()))
r.write('\nОбщие отгрузки:\n')
r.write(str(total_out()))
r.write('\nТовары с отрицательным остатком:\n')
r.write(str(f4_1()))
r.write('\nТовары без поступлений, но с отгрузкой:\n')
r.write(str(f4_2()) + '\n')
r.write(str(f5_1()))
r.write('\nДаты операций с яблоками:')
r.write(str(f6()))


