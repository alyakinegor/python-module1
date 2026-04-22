import random
wins = [
        (0,1,2), (3,4,5), (6,7,8), (0,4,8),(2,4,6),(1,4,7),(0,3,6),(2,5,8)
    ]
def nums(b):
    nums = []
    for el in b:
        if el.isdigit():
            nums.append(el)
    return nums
    
def is__player_winner(a):
    for el in wins:
        if set(el).issubset(set(a)):
            return True

def is__bot_winner(b):
    for el in wins:
        if set(el).issubset(set(b)):
            return True
        
def game():
    board = """ 0 | 1 | 2 
 3 | 4 | 5
 6 | 7 | 8"""
    
    arr_p = []
    arr_c = []
    cont = True
    while cont:
        print(board)
        num = int(input('введите цифру вашего хода: '))
        arr_p.append(num)
        board = board.replace(str(num), 'К')
        arr = nums(board)
        if is__player_winner(arr_p):
            print('игрок выиграл')
            return 
        try:
            comp_num = random.choice(arr)
        except IndexError:
            print('ничья')
            return
        print('комп выбрал: ', comp_num)
        arr_c.append(int(comp_num))
        board = board.replace(str(comp_num), 'Н')
        arr = nums(board)
        if is__bot_winner(arr_c):
            print('бот выиграл')
            return 
        
game()
