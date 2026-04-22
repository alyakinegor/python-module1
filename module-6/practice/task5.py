obj = {
    'me': {'rodion', 'anton', 'arina'},
    'rodion':{'anton', 'me', 'misha', 'vadim'},
    'anton': {'rodion', 'me','ruslan'},
    'arina': {'marina', "nadia", 'dasha'},
    'dasha': {'anna', 'lera', 'nadia'}
    

}
s = input()
friends = obj[s]
res = set()
for el in friends:
    res.update(obj[el])
res.discard(s)
res -= friends
print(res)
