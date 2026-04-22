
workers = [(1,'Осипов А.Н',24),
           (2,'Петров В.А',20),
           (3,'Николаев П.Е',18)
]

def add_worker():
    id = int(input('введите ID: '))
    name = input('введите имя: ')
    age = int(input('введите возраст: '))
    t = tuple([id,name, age])
    workers.append(t)

def delete_worker(w_id):
    for el in workers:
        if el[0] == w_id:
            workers.remove(el)
    
def print_info():
    for el in workers:
        print('ID -',el[0])
        print('name -',el[1])
        print('age -',el[2])
    
def find_by_age(year):
    for el in workers:
        if el[2] == year:
            print(el)

def find_by_Lastname(char):
    for el in workers:
        if el[1][0] == char:
            print(el)

def save():
    with open('workers_log.txt', 'w', encoding='utf-8') as f:
        for el in workers:
            line = ''
            for i in el:
                line += str(i) + ','
            f.write(line[:-1] + '\n')

def pull():
    with open('workers_log.txt', 'r', encoding='utf-8') as f:
        workers.clear()
        for line in f.read().split('\n'):
            if line != '':
                line = line.split(',')
                line[0], line[2] = int(line[0]), int(line[2])
                workers.append(tuple(line))



def run():
    print("""Введите:
               1 - Добавить сотрудника
               2 - Удалить сотрудника
               3 - Вывести всех сотрудников
               4 - Поиск по возрасту
               5 - поиск по фамилии
               6 - сохранить
               7 - выйти""")
    ch = 0
    while ch != 7:
        ch = int(input())
        if ch == 1:
            add_worker()
        elif ch == 2:
            i  = int(input('Введите ID для удаления: '))
            delete_worker(i)
        elif ch == 3:
            print_info()
        elif ch == 4:
            i = int(input('Введите возраст: '))
            find_by_age(i)
        elif ch == 5:
            char = input('Введите первую букву: ')
            find_by_Lastname(char)
        elif ch == 6:
            save()
        else:
            save()
            break
        print('Что дальше?')

run()