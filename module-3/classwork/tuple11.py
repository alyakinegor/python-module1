old = {'A': 100, "B": 200, 'C': 300, 'D': 400}
new = {'B': 220, "C": 310, 'E': 500, 'F': 600}
only_in_new = []
only_in_old = []
for el in new.keys():
    if el not in old.keys():
        only_in_new.append(el)
for el in old.keys():
    if el not in new.keys():
        only_in_old.append(el)
    else:
        print(f'разница цен у ключа {el}:{new[el]}-{old[el]}={new[el]-old[el]}')
print('только в новом', only_in_new)
print('только в старом', only_in_old)
