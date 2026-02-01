cods = [3,4,6,7,5,2,1]
numbers = [79603064931, 79653155551, 79001454948, 79803201520, 79453554555, 71234567890, 79303206070]
users_data_cods = {
    3:79603064931,
    4:79653155551,
    6:79001454948,
    7:79803201520,
    5:79453554555,
    2:71234567890,
    1:79303206070
}
user_data_phones = {
    79603064931:3,
    79653155551:4,
    79001454948:6,
    79803201520:7,
    79453554555:5,
    71234567890:2,
    79303206070:1
}
n = True
while n:
    print('''
    1.сортировать по кодам
    2.сортировать по номерам
    3.вывести список пользователей
    4.Выход
    ''')
    ch = int(input())
    if ch == 4:
        n = False
    elif ch == 3:
        print('сортировка по кодам: ')
        for el in cods:
            print(f'user_{el}: code - {el}; phone number - {users_data_cods[el]}')
        print('сортировка по телефонам: ')
        for el in numbers:
            print(f'user_{user_data_phones[el]}: code - {user_data_phones[el]}; phone number - {el}')
    elif ch == 2:
        numbers.sort()
    elif ch == 1:
        cods.sort()
    