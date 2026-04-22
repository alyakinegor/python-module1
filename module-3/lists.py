l = [-1,-2,-3,4,5,6,7,8,9,10]
s = [0 if x < 0 else x for x in l]
res = []
for el in l:
    res.append(el**2)
print(s)