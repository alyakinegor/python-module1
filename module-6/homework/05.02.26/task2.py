import random
def create_number():
    return random.randint(1000,9999)
def game():
    n = create_number()
    def rec():

        p = int(input())
        if n == p:
            print('Вы угадали!')
            return
        else:
            bulls = []
            cows = []
            check = str(n)
            for el in range(4):
                if check[el] == str(p)[el]:
                    bulls.append(int(str(p)[el]))
                    check.replace(check[el], '')
                elif str(p)[el] in check:
                    cows.append(int(str(p)[el]))
        print(f'{bulls}-на своем месте \n{cows}-есть в числе, не на своем месте \n   1.Играть дальше \n   2.Выйти из игры')
        ch = int(input())
        if ch == 2:
            return
        else:
            rec()

    rec()
            
game()