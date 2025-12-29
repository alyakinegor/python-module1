text = 'Hello world!'
rep = {'e': 1, "l": 0, 'o': 2, 'r': '3'}
res = ''
for i in text:
    res += str(rep.get(i, i))
print(res)