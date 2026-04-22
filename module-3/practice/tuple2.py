s = input()
n = 0
c = 0
for el in s:
    if el.isalpha():
        c+=1
    elif el.isdigit():
        n+=1
print(f'Букв: {c}, цифр:{n}')
