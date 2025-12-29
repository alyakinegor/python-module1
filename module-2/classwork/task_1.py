s= input()
l = list(s)
d = {}
for el in l:
    d.setdefault(el, 0)
    d[el] += 1
for el, v in d.items():
    print(f'{el}={v}')