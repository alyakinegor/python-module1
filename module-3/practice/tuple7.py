elems = list(map(int, input('введите елементы массива: ').replace(' ', '')))
el = int(input())
c = 0
for i in elems:
    if el ==i:
        c += 1
print(c)