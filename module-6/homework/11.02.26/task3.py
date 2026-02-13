people = [
    {'name': 'Иванов Иван Иванович', 'phone': '79603064931', 'post': 'manager', 'email': 'd@gmail.com', 'cub': '315', 'skype': 1},
    {'name': 'Петрова Мария Сергеевна', 'phone': '79003085067', 'post': 'accountat', 'email': 'a@gmail.com', 'cub': '300', 'skype': 2},
    {'name': 'Антонов Кирилл Семенович', 'phone': '79803054637', 'post': 'guardian', 'email': 'c@gmail.com', 'cub': '100', 'skype': 3}
]

def add(name, phone=None, post=None, email=None, cub=None, skype=None):
    res = {'name': name, 'phone': phone, 'post': post, 'email': email, 'cub': cub, 'skype': skype}
    people.append(res)

def delete_user(name):
    for el in people:
        if el['name'] == name:
            people.remove(el)

def search(name, keyword):
    for el in people:
        if el['name'] == name:
            for key in el.keys():
                if key == keyword:
                    print(el[key])

def swap_data(name, key_for_swap, newVal):
    for el in people:
        if el['name'] == name:
            el[key_for_swap] = newVal

add('Питер')
swap_data('Питер', 'phone', "000000000")
search('Питер', 'phone')
# print(people)