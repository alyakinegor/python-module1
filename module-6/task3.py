arr = ('mercedes', 'audi', 'audi++')
s = input()
rep = input()
res = list(arr)
for el in res:
    if el == s:
        res.remove(el)
        res.append(rep)

print(res)