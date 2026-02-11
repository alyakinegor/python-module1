"""
ЗАДАЧА: Анализ успеваемости студентов

Каждая запись содержит:
- name    : имя студента
- subject : предмет
- score   : оценка (0–100)

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Для каждого студента:
   - посчитать средний балл
   - определить, сдал ли он экзамены
     (экзамен считается сданным, если score >= 60 по ВСЕМ предметам)

2. Для каждого предмета:
   - посчитать средний балл
   - найти лучшего студента по этому предмету

3. Найти студентов, у которых:
   - средний балл >= 85
   - и нет ни одного несданного предмета

4. Найти студента с:
   - самым высоким средним баллом
   - самым низким средним баллом
"""

students = [
    {"name": "Алиса", "subject": "математика", "score": 85},
    {"name": "Боб",   "subject": "математика", "score": 72},
    {"name": "Алиса", "subject": "физика",     "score": 90},
    {"name": "Боб",   "subject": "физика",     "score": 60},
    {"name": "Алиса", "subject": "информатика","score": 95},
    {"name": "Боб",   "subject": "информатика","score": 88},
    {"name": "Кира",  "subject": "математика", "score": 40},
    {"name": "Кира",  "subject": "физика",     "score": 55},
]

def func1():
   res = {}
   for el in students:
      res.setdefault(el['name'], {'avg_score': [], 'isPass': True})
      res[el['name']]['avg_score'].append(el['score'])
      if el['score'] < 60:
         res[el["name"]]['isPass'] = False
   for el in res.keys():
      arr = res[el]['avg_score']
      res[el]['avg_score'] = sum(arr) / len(arr)
   return res

def func2():
   m = 0
   res = {}
   for el in students:
      res.setdefault(el['subject'], {'avg_score': [], 'best_student': ''})
      if el['score'] > m:
         res[el["subject"]]['best_student'] = el['name']
         m = el['score']
      res[el["subject"]]['avg_score'].append(el['score'])
   for el in res.keys():
      arr = res[el]['avg_score']
      res[el]['avg_score'] = sum(arr) / len(arr)
   return res

print(func2())

   