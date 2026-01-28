arr = {1,5,8,7,4}
obj = {
    5: 'джекпот',
    4: 'Золото',
    3: 'Серебро',

}
choice = set(map(int, input().split()))
res = len(arr) - len(arr - choice)
print(obj.get(res))