s = input()
arr = ['+', '-', '/', '*']
for el in arr:
    if el in s:
        arr2 = list(map(int, s.split(el)))
        if el == '+':
            print(arr2[0]+arr2[1])
        elif el == '-':
            print(arr2[0]-arr2[1])
        elif el == '/':
            print(arr2[0]/arr2[1])
        elif el == '*':
            print(arr2[0]*arr2[1])
        break

