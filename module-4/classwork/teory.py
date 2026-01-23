# def func_1():
#     print('hello world')
# def func_2():
#     return 1
# def func_3(name, a, b):
#     print(name, a, b)
# def func_4(*args):
#     print(args)
# def func_7(**kwargs):
#     print(kwargs)

def func_8(num1, num2, *args, **kwargs):
    print(f'{num1}-{num2}-{args}-{kwargs}')

def func_9(obj):
    print(obj)

func_8(1,2,3,4,5,6,7, name='alex')
func_9({'a':1, 'b':2})
# func_7(name='alex', age=12)
# func_1()
# print(func_2())
# func_3('alex', 'a', 'b')
# func_4(1,2,3,4,5,6)