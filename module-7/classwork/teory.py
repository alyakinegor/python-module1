# file = open('file.txt', 'r')
# print(file.read(2))
# print(file.read(1))
# file.close()

# # r - чтение
# # w - запись с очисткой
# # a - дозапись текста в конец 
# # x - создает новый файл
# # b - бинарный режим
# # t - текстовый вариант
# #  + - чтение и запись

# file = open('file.txt', 'a', encoding='utf-8')
# file.write(' конец')
# file.close()

# f = open('file.txt', 'a', encoding='utf-8')
# f.write('1,2,3\n')
# f.write('4,5,6\n')
# f.write('7,8,9')
# f.close()
# f = open('file.txt', 'r', encoding='utf-8')
# print(f.readline().strip())
# print(f.readline().strip())
# for line in f:
#     print(line.strip())

with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())