li = [1, 2, 4, -6, -2]
def sum_negative(l):
    res = 0
    for el in l:
        if el < 0:
            res += el
    return res

def sum_even(l):
    res = 0
    for el in l:
        if el % 2 == 0:
            res += el
    return res

def sum_not_even(l):
    res = 0
    for el in l:
        if el % 2 != 0:
            res += el
    return res

def func4(l):
    c = 1
    for el in l:
        if l.index(el) % 3 == 0:
            c *= el
    return c

def func5(l: list):
    l = sorted(l)[1:-1]
    c = 1
    for el in l:
        c *= el
    return c

def func6(l: list):
    first = None
    last = None
    for el in l:
        if el > 0:
            first = l.index(el)
            break
    new = l[::-1]
    for i in new:
        if i > 0:
            last = new.index(i)
            break
    l = l[first + 1:last]
    return sum(l)

print(func6(li))
print(func5(li))
print(func4(li))
print(sum_not_even(li))
print(sum_even(li))
print(sum_negative(li))