d = {
    'a': 1,}
d.update({'a': 2, 'b': 3})
d.update(c=4, d=5)
if not 'a' in d:
    print('ok')
print(d.keys())
print(d.values())
for l ,v in d.items():
    print(f'{l}={v}')