li = [1, 2, 0, -4, -6, 0]
c_negative = 0
c_positive = 0
c_null = 0
print(f'минимальное: {min(li)}')
print(f'максимальное: {max(li)}')
for el in li:
    if el <0:
        c_negative += 1
    elif el > 0:
        c_positive += 1
    else:
        c_null += 1
print(f'положительных: {c_positive}')
print(f'отрицательных: {c_negative}')
print(f'нулей: {c_null}')