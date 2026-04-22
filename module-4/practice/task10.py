def func(li):
    new = []
    for el in li:
        for i in el:
            new.append(i)
    print(new)

func([[1,2,3], [2,4]])