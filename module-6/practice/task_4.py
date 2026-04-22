books = [
    {'author': 'Александр Сергеевич Пушкин', 'name': 'Повести Белкина', 'year': 1831, 'pages': 128, 'publish_by': 'Азбука', 'genre': 'повесть'},
    {'author': 'Лев Николаевич Толстой', 'name': 'Война и мир', 'year': 1869, 'pages': 1300, 'publish_by': 'Эксмо', 'genre': 'роман'},
    {'author': 'Фёдор Михайлович Достоевский', 'name': 'Преступление и наказание', 'year': 1866, 'pages': 672, 'publish_by': 'АСТ', 'genre': 'роман'},
    {'author': 'Михаил Афанасьевич Булгаков', 'name': 'Мастер и Маргарита', 'year': 1967, 'pages': 480, 'publish_by': 'Азбука', 'genre': 'роман'},
    {'author': 'Антон Павлович Чехов', 'name': 'Вишнёвый сад', 'year': 1904, 'pages': 96, 'publish_by': 'Речь', 'genre': 'пьеса'},
]

def add(name, author=None, year=None, pages=None, publish_by=None, genre=None):
    res = {'author': author, 'name': name, 'year': year, 'pages': pages, 'publish_by': publish_by, 'genre': genre}
    books.append(res)

def delete_book(name):
    for el in books:
        if el['name'] == name:
            books.remove(el)

def search(name, keyword):
    for el in books:
        if el['name'] == name:
            for key in el.keys():
                if key == keyword:
                    print(el[key])

def swap_data(name, key_for_swap, newVal):
    for el in books:
        if el['name'] == name:
            el[key_for_swap] = newVal

add('Книга1')
swap_data('Книга1', 'author', "Виктор")
search('Книга1', 'author')
# print(books)