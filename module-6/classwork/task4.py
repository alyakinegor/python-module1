tpl = (1,3,13,344,1323,1233)
obj = {}
for el in tpl:
    obj.setdefault(len(str(el)), 0)
    obj[len(str(el))] += 1
print(obj)