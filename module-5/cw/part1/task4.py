logs = [
    ('ivan', 'day', 1),
    ('ivan', 'night', 4),
    ('olga', 'day', 1),
    ('petr', 'night', 1),
    ('anna', 'day', 9),
    ('anna', 'day', 3),
]

def func1():
    days = set()
    night = set()
    for el in logs:
        if el[1] != 'day':
            night.add(el[0])
        else:
            days.add(el[0])
    return days ^ night

def func2():
    days = 0
    nights = 0
    res = []
    for el in logs:
        if el[1] == 'day':
            days += el[2]
        else:
            nights += el[2]
    if days < 8:
        res.append('day')
    if nights < 8:
        res.append('night')
    return res


def func3():
    res  ={}
    ans = []
    for el in logs:
        res.setdefault(el[0], 0)
        res[el[0]] += el[2]
    for i in res.keys():
        if res[i] >= 12:
            ans.append(i)
    return ans

print(func1())
print(func2())
print(func3())
arr = [1,4,6,6,2]
arr.remove(6)
print(arr)