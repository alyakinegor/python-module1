def paint(l, direct, symbol):
    res = ''
    if direct == 'vertical':
        res = (symbol + '\n') * l
    else:
        res = symbol * l
    print(res)
paint(10, 'vertical', '|')
paint(10, 'gorisontal', '|')