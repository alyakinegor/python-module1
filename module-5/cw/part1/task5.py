history = [
    ('t_1', 'new'), ("t_1", 'in progress'),
    ('t_1', 'done'),
    ('t_2', 'new'), ('t_2', 'done'),
    ('t_3', 'new'), ('t_3', 'in progress'), ('t_3', 'cancelled'),
    ('t_4', 'new'), ('t_4', 'cancelled'),('t_4', 'done')
    ]

for i in range(1, 5):
    arr = []
    for el in history:
        if el[0] == f't_{i}':
            arr.append(el[1])
    for j in range(len(arr) -1):
        if (arr[j] == 'new' and arr[j+1]=='in progress') or (arr[j] == 'in progress' and arr[j+1]=='done') or (arr[j] == 'new' and arr[j+1]=='cancelled') or (arr[j] == 'in progress' and arr[j+1]=='cancelled'):
            pass
        else:
            print(f't_{i}')