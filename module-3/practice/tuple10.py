li = [1, 2, 4, -6, -2]
def arr_even(l):
    res = []
    for el in l:
        if el % 2 == 0:
            res.append(el)
    return res

def arr_not_even(l):
    res = []
    for el in l:
        if el % 2 != 0:
            res.append(el)
    return res

def arr_positive(l):
    res = []
    for el in l:
        if el > 0:
            res.append(el)
    return res

def arr_negative(l):
    res = []
    for el in l:
        if el < 0:
            res.append(el)
    return res

print(arr_even(li))
print(arr_not_even(li))
print(arr_positive(li))
print(arr_negative(li))