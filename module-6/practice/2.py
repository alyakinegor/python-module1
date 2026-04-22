logs = [
    ('ivan', 'd1', 'login'),
    ('ivan', 'd1', 'view'),
    ('ivan', 'd2', 'login'),
    ('olga', 'd1', 'login'),
    ('petr', 'd2', 'error'),
    ('anna', 'd1', 'login'),
    ('anna', 'd1', 'view'),
]
import math
obj_users = {}
obj_day = {}
for el in logs:
    obj_users.setdefault(el[0], [])
    obj_users[el[0]].append(el[2])

    obj_day.setdefault(el[0], [])
    obj_day[el[0]].append(el[1])
    
def has_error_and_no_login():
    arr = []
    for el in obj_users:
        if 'error' in obj_users[el] and 'login' not in  obj_users[el]:
            arr.append(el)
    print(arr)

def activity():
    obj_days = {}
    res = []
    for el in logs:
        obj_days.setdefault(el[0], [])
        obj_days[el[0]].append(el[1])
    for i in obj_days:
        if len(obj_days[i]) > 1:
            res.append(i)
    print(res)

def minimal_activity():
    obj_days = {}
    res = []
    for el in logs:
        obj_days.setdefault(el[1], [])
        obj_days[el[1]].append(el[0])
    m = math.inf
    for el in obj_days:
        if len(obj_days[el]) < m:
            m = len(obj_days[el])
    for el in obj_days:
        if len(obj_days[el]) == m:
            res.append(el)
    print(res)


def raport():
    res_obj = {}
    for el in logs:
        res_obj.setdefault(el[0],  {'action count': None, 'days': [], 'actions': set()})
        res_obj[el[0]]['action count'] = len(obj_users[el[0]])
        res_obj[el[0]]['days'] = obj_day[el[0]]
        res_obj[el[0]]['actions'].update(obj_users[el[0]])
    print(res_obj)

has_error_and_no_login()
activity()
minimal_activity()
raport()