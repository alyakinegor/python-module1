clients = [
    (1, '111', 'a@x.com'),
    (2, '111', 'b@x.com'),
    (3, '222', 'c@x.com'),
    (4, '333', 'c@x.com'),
    (5, '444', 'd@x.com')
]

def dubles():
    obj_phones = {}
    obj_mail = {}
    d_phone = []
    d_mail = []
    no_d = []
    for el in clients:
        obj_phones.setdefault(el[1], set())
        obj_phones[el[1]].add(el[0])
        obj_mail.setdefault(el[2], set())
        obj_mail[el[2]].add(el[0])
    for el in obj_phones.values():
        if len(el) > 1:
            d_phone.extend(el)
    for el in obj_mail.values():
        if len(el) > 1:
            d_mail.extend(el)
    for i in obj_phones.values(): 
        if len(i) == 1 and list(i)[0] not in d_mail:
            no_d.append(list(i)[0])
    print(f'дубли по телефонам:{d_phone}')
    print(f'дубли по почте: {d_mail}')
    print(f'без дублей:{no_d}')
    print(f'количество: {len(no_d)}')

'aa'.zfill
dubles()