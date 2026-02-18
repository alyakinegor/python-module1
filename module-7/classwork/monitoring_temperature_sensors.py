"""
ЗАДАЧА: Мониторинг температуры датчиков

Даны показания температурных датчиков.

Каждая строка файла имеет формат:
датчик,дата,температура

Где:
- датчик      — идентификатор датчика
- дата        — дата измерения (YYYY-MM-DD)
- температура — целое число

Показания:
sensor1,2024-01-01,22
sensor1,2024-01-01,27
sensor2,2024-01-01,19
sensor3,2024-01-01,35
sensor1,2024-01-02,31
sensor2,2024-01-02,29
sensor3,2024-01-02,40
sensor1,2024-01-03,25
sensor3,2024-01-03,38


НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Записать показания в файл sensors.log

2. Прочитать файл sensors.txt и загрузить данные.

3. Для каждого датчика:
   - определить минимальную температуру
   - максимальную температуру
   - среднюю температуру

4. Найти датчики, у которых хотя бы раз
   температура была выше 30 градусов.

5. Для каждой даты посчитать среднюю температуру
   по всем датчикам и найти день
   с самой высокой средней температурой.

6. Найти датчики, которые работали НЕ каждый день
   (т.е. у них есть пропущенные даты).

7. Записать подробный отчёт в файл sensors_report.txt.
"""
logs = ['sensor1,2024-01-01,22',
        'sensor1,2024-01-01,27',
        'sensor2,2024-01-01,19',
        'sensor3,2024-01-01,35',
        'sensor1,2024-01-02,31',
        'sensor2,2024-01-02,29',
        'sensor3,2024-01-02,40',
        'sensor1,2024-01-03,25',
        'sensor3,2024-01-03,38']


with open('sensors.log', 'w', encoding='utf-8') as file:
    file.write('\n'.join(logs))

f = open('sensors.log', 'r', encoding='utf-8')
a = f.read().split('\n')

logs.clear()
for line in a:
   logs.append(line)

sensors = {}
warm_sensors = set()
dates = {}
max_average_temp = 0
day = None
for el in logs:
   arr = el.split(',')
   sensors.setdefault(arr[0], {'values': [], 'max': 0, 'min': 0, 'average': 0})
   sensors[arr[0]]['values'].append(int(arr[-1]))
   sensors[arr[0]]['max'] = max(sensors[arr[0]]['values'])
   sensors[arr[0]]['min'] = min(sensors[arr[0]]['values'])
   sensors[arr[0]]['average'] = sum(sensors[arr[0]]['values']) / len(sensors[arr[0]]['values'])
   #-------------
   if int(arr[-1]) > 30:
      warm_sensors.add(arr[0])
   #----------------
   dates.setdefault(arr[1], 0)
   temps = []
   temps.append(int(arr[-1]))
   dates[arr[1]] = sum(temps) / len(temps)



for key in dates.keys():
   if dates[key] > max_average_temp:
      max_average_temp = dates[key]
      day = key
print(day)