"""
ЗАДАЧА: Умный контроль доступа (бейджи)

Даны записи содержащие журнал проходов сотрудников.

Каждая строка файла имеет формат:
дата,имя,действие

Где:
- дата     — строка в формате YYYY-MM-DD
- имя      — имя человека
- действие — ENTER (вход) или EXIT (выход)

Журнал проходов:
2026-02-01,Иван,ENTER
2026-02-01,Мария,ENTER
2026-02-01,Иван,EXIT
2026-02-01,Иван,EXIT
2026-02-01,Олег,EXIT
2026-02-02,Мария,EXIT
2026-02-02,Олег,ENTER

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Записать проходы в файл access.log

2. Прочитать файл access.log и загрузить данные.

3. Для каждого человека:
   - посчитать количество входов (ENTER)
   - посчитать количество выходов (EXIT)
   - определить, находится ли человек ВНУТРИ в конце лога
     (ENTER без последующего EXIT)

4. Найти людей с ошибками доступа:
   - EXIT без предварительного ENTER
   - два ENTER подряд без EXIT
   (сохранить таких людей в множество)

5. Для каждой даты посчитать количество входов (ENTER).

6. Найти дату с максимальным количеством входов.

7. Записать подробный отчёт в файл access_report.txt.
"""

logs = ['2026-02-01,Иван,ENTER',
        '2026-02-01,Мария,ENTER',
        '2026-02-01,Иван,EXIT',
        '2026-02-01,Иван,EXIT',
        '2026-02-01,Олег,EXIT',
        '2026-02-02,Мария,EXIT',
        '2026-02-02,Олег,ENTER']


with open('access.log', 'w', encoding='utf-8') as file:
    file.write('\n'.join(logs))

f = open('access.log', 'r', encoding='utf-8')
a = f.read().split('\n')

logs.clear()
for line in a:
    logs.append(line)

def f3():
   res = {}
   for el in logs:
      is_inside = None
      arr = el.split(',')
      res.setdefault(arr[1], {'EXIT':0, 'ENTER': 0})
      
      if 'EXIT' in arr:
         res[arr[1]]['EXIT'] += 1
         is_inside = False
      else:
         res[arr[1]]['ENTER'] += 1
         is_inside = True
      res[arr[1]]['IS_INSIDE'] = is_inside
   return res

def f4():
   res = {}
   s = set()
   for el in logs:
      arr = el.split(',')
      res.setdefault(arr[1], [])
      res[arr[1]].append(arr[2])
   for key in res.keys():
      arr = res[key]
      l = []
      for el in arr:
         if el == 'ENTER':
            l.append('1')

         elif el == 'EXIT':
            if len(l) == 0:
               s.add(key)
            else:
               l.remove(l[-1])
         if '11' in ''.join(l):
            s.add(key)
   return s
         
def f5():
   res = {}
   for el in logs:
      arr = el.split(',')
      res.setdefault(arr[0], 0)
      if 'ENTER' in arr:
         res[arr[0]] += 1
   return res

def f6():
   res = f5()
   m = 0
   k = None
   for key in res.keys():
      if res[key] > m:
         m = res[key]
         k = key
   
   return k


def write_report():
   r = open('access_report.log', 'w', encoding='utf-8')
   res = f3()
   for k in res.keys():
      line = f'{k}: Входы: {res[k]['ENTER']}; Выходы: {res[k]['EXIT']}'
      r.write(line + '\n')
   res2 = f4()
   r.write('Люди с ошибочной записью: ')
   line = ''
   for el in res2:
      line += el + ', '
   r.write(line[:-2] + '\n')
   r.write('Количество входов по датам: ')
   res3 = f5()
   line = ''
   for k in res3.keys():
      line += k
      line += f': {res3[k]}; '
   r.write(line[:-2] + '\n')
   r.write(f'Дата с максимальным количеством входов: {f6()}')

   

   
write_report()
   


