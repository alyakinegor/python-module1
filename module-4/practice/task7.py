def is_happy(n):
    p1 = list(map(int, n[0:3]))
    p2 = list(map(int, n[3:]))
    if sum(p1) == sum(p2):
        return True
    else: 
        return False
print(is_happy('123420'))