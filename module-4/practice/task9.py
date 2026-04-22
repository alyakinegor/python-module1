def func(s):
    obj = {}
    for el in s:
        obj.setdefault(s.count(el), el)
    return obj[max(obj.keys())]

print(func('Hello worldd')) 