logs = [
    ("ivan", 8), ("ivan", 10),
    ("olga", 20),
    ("petr", 45),
]

def get_hours():
    res = {}
    for el in logs:
        res.setdefault(el[0], 0)
        res[el[0]] += el[1]
    return res

def work():
    res = get_hours()
    arr1 = []
    arr2 = []
    for key in res.keys():
        if res[key] > 40:
            arr1.append(key)
        elif res[key] < 20:
            arr2.append(key)

    return f'Перервботка: {arr1}, недоработка: {arr2}'


