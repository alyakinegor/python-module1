import random
tasks = []
for i in range(10):
    tasks.append({
        'id': i,
        'assignee': random.choice(['ivan', 'olga', 'petr', 'anna', 'oleg']),
        'status': random.choice(['in progress', 'blocked', 'in review', 'waiting vendor']),
        'days in status': random.randint(0, 10)

    })
def func1():
    res = []
    for el in tasks:
        if 'in progress' in el['status'] and el['days in status'] > 7:
            res.append(el['assignee'])
    return res

def func3():
    res = {
        'in progress': [],
        'blocked': [],
        'in review': [],
        'waiting vendor': []
    }
    ans = []
    for el in tasks:
        res[el['status']].append(el['assignee'])
    for i in res.keys():
        if len(res[i]) == 1:
            ans.append(i)
    return ans

def func4():
    res = {
    
    }
    for el in tasks:
        res.setdefault(el['assignee'], 0)
        if el['status'] == 'in progress' or el['status'] == 'blocked':
            res[el['assignee']] += el['days in status']
    m = 0
    name = None
    for i in res.keys():
        if res[i] > m:
            m = res[i]
            name = i
    print(res)
    return name



print(func1())
print(func3())
print(func4())
