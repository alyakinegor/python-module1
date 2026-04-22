def count_sentenses(text):
    s = '.!?'
    c = 0
    prev = ''
    for el in text:
        if el in s:
            c+= 1
            prev += el
        if len(prev) == 3:
            if prev == '...':
                c -= 2
                prev = ''
            else:
                prev = ''
    return c



print(count_sentenses('hello world. what a nice day! aaaa bbbb... aaaa bb.'))