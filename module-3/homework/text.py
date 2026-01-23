# def text(text: str, *words):
#     li = text.split(' ')
#     print(words)
#     for el in li:
#         if el in words:
#             index = li.index(el)
#             li.pop(index)
#             li.insert(index, el.capitalize())
#             print(el)
#     print(' '.join(li))

# text('hello world. what a nice day!', 'hello', 'world')

def txt(s: str, *wrd: list):
    res = s
    for el in wrd:
        if el in s:
            p1 = res.split(el)[0]
            p2 = res.split(el)[1]
            res = p1 + el.capitalize() + p2
    print(res)

txt('hello world. what a nice day!', 'hello', 'world', 'day')