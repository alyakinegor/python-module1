board = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]

v = [(2, 1),(2, -1), (1, 2), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
x = None
y = None
i = 1
curr_x = None
curr_y = None
obj = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
}
def put_horse(k):
    global x, y, i, curr_x, curr_y

    y = obj[k[0]]
    x = 8 - int(k[1])
    print(x, y)
    board[x][y] = i
    curr_x = x
    curr_y = y
    i+=1

# x - выбирает массив в массиве #x - 0
# y - выбирает индекс в массиве# y - obj[y] = 0
def check():
    cont = False
    for el in board:
        if 0 in el:
            cont = True
    return cont
def func():
    for j in v:
        for el in v:
            global x, y,i,curr_y,curr_x
            x = curr_x +  el[0]
            y = curr_y +  el[1]
            try:
                if board[x][y] == 0:
                    board[x][y] = i
                    i += 1  
                    curr_x = x
                    curr_y = y
            except IndexError:
                pass
        



            

put_horse('d4')
func()
for i in board:
    print(i)

