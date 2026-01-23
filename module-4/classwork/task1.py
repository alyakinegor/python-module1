def func(n1, n2):
    c = n1
    while c < n2:
        if c % 2 != 0:
            print(c)
            c+=1
        else:
            c+=1

func(10, 15)