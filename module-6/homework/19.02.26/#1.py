payments = [
    ("ivan", 100),
    ("ivan", -30),
    ("ivan", -20),
    ("olga", 200),
    ("petr", -50),
]
def get_balance():
    res = {}
    for el in payments:
        res.setdefault(el[0], 0)
        res[el[0]] += el[1]
    return res

def negative_balance():
    arr = []
    res = get_balance()
    for key in res.keys():
        if res[key] < 0:
            arr.append(key)
    return arr

def count_operations():
    set1 = set()
    res = {}
    for el in payments:
        res.setdefault(el[0], 0)
        res[el[0]] += 1
        if res[el[0]] > 2:
            set1.add(el[0])

    return set1

print(count_operations())