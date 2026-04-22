def summ(start, end):
    res = 0
    for x in range(start+1, end):
        res += x
    print(res)

summ(10, 12)