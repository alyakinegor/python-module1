def func(a, b):
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    return func(b, a % b)

print(func(50,18))