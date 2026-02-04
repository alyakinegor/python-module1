board = [[0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
]

curr_x = None
curr_y = None
x = 0
y = 0
j = 1
v = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
def put_horse(a, b):
    global curr_y, curr_x, x, y, j
    y = 8 - b
    x = a - 1
    curr_x, curr_y = x, y
    board[y][x] = j
    j += 1

put_horse(1, 8)

def show():
    for i in board:
        print(i)
# def func():
#     global x, y, j, curr_x, curr_y
while True:
    for i in v:
        x = curr_x + i[0]
        y = curr_y + i[1]
        if len(board) > y and y >= 0 and len(board[0]) > x and x >= 0:
            if board[y][x] == 0:
                board[y][x] = j
                j += 1
            curr_x = x
            curr_y = y
        else:
            x = curr_x
            y = curr_y
    arr = []
    for el in board:
        arr.extend(el)
    if 0 not in arr:
        break
    show()
    print('-----------------------------------')



