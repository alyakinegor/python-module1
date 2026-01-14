n = [0,1,2,3,4,5,6,7,8,9,10]
med = sum(n) / len(n)
res = [x for x in n if x > med]
print(med)
print(res)