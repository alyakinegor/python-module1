txt = 'hello wolrd1. what a nice day! AAAAA'
def cap(s: str):
    l = s.split('. ')
    res = ''
    for el in l:
        res += el.capitalize()
        if el[-1] not in '!?':
            res += '. '
    return res

def digits(s):
    c = 0
    for el in s:
        if el.isdigit():
            c += 1
    return c

def signs(s):
    sgn = ',.!?-;:'
    c = 0
    for el in s:
        if el in sgn:
            c += 1
    return c

def sp_sign(s):
    c = 0
    for el in s:
        if '!' == el:
            c += 1
    return c

print(cap(txt))
print(digits(txt))
print(signs(txt))
print(sp_sign(txt))


