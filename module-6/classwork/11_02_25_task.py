
# ЗАДАЧА: Анализ чатов пользователей

# Даны сообщения в чате. Каждое сообщение представлено словарём
# со следующими ключами:
# - "user"      : имя пользователя (строка)
# - "text"      : текст сообщения (строка)
# - "timestamp" : время сообщения (целое число, возрастает не строго)

# Пример входных данных:
# messages = [
#     {"user": "Алиса", "text": "привет здравствуй",     "timestamp": 1},
#     {"user": "Боб",   "text": "здравствуй",            "timestamp": 2},
#     {"user": "Алиса", "text": "как дела у тебя",       "timestamp": 3},
#     {"user": "Боб",   "text": "привет Алиса",          "timestamp": 4},
#     {"user": "Алиса", "text": "привет привет здравствуй", "timestamp": 10},
#     {"user": "Боб",   "text": "пока",                  "timestamp": 20},
# ]

# НЕОБХОДИМО РЕАЛИЗОВАТЬ:

# 1. Посчитать количество сообщений каждого пользователя.
#    Результат сохранить в словарь вида:
#    {
#        "Алиса": 3,
#        "Боб": 2
#    }

# 2. Для каждого пользователя:
#    2.1 Найти множество уникальных слов, которые он использовал
#        (слова разделяются методом split()).
#    2.2 Найти самое частое слово пользователя.
#        Если самых частых слов несколько — можно выбрать любое.

# 3. Найти пользователя с самым большим словарным запасом,
#    где словарный запас — это количество уникальных слов,
#    использованных пользователем.

# 4. Найти множество слов, которые использовали ВСЕ пользователи
#    (пересечение множеств слов пользователей).

# 5. Для каждого пользователя определить максимальный перерыв
#    между его сообщениями:
#    - перерыв = разница между timestamp текущего и предыдущего сообщения
#    - найти пользователя с самым большим таким перерывом

messages = [
    {"user": "Алиса", "text": "привет здравствуй",     "timestamp": 1},
    {"user": "Боб",   "text": "здравствуй",            "timestamp": 2},
    {"user": "Алиса", "text": "как дела у тебя",       "timestamp": 3},
    {"user": "Боб",   "text": "привет Алиса",          "timestamp": 4},
    {"user": "Алиса", "text": "привет привет здравствуй", "timestamp": 10},
    {"user": "Боб",   "text": "пока",                  "timestamp": 20},
]
def count_messages():
    res = {}
    for i in messages:
        res.setdefault(i['user'], 0)
        res[i["user"]] += 1
    return res

def different_and_frequent_words():
    res = {}
    # 2.1
    for i in messages:
        res.setdefault(i['user'], {'unique_words': set(), 'frequent_word': {}})
        res[i["user"]]['unique_words'].update(i['text'].split(' '))
        for el in i["text"].split():
            freq = res[i["user"]]['frequent_word']
            freq.setdefault(el, 0)
            freq[el] += 1
    #2.2
    for j in res.keys():
        obj = res[j]['frequent_word']
        max = 0
        for v in obj.values():
            if v >  max:
                max = v
        for el in obj.keys():
            if obj[el] == max:
                res[j]['frequent_word'] = el
                break
    return res
        
def find_biggest_dict():
    res = different_and_frequent_words()
    m = 0
    user = ''
    for key in res.keys():
        if len(res[key]['unique_words']) > m:
            m = len(res[key]['unique_words'])
            user = key
    return user

def general_words():
    res = different_and_frequent_words()
    set_1 = res['Алиса']['unique_words']
    set_2 = res['Боб']['unique_words']
    return set_1.intersection(set_2)

def break_before_sms():
    res = {}
    for i in messages:
        res.setdefault(i['user'], [])
        res[i["user"]].append(i['timestamp'])
    for el in res.keys():
        arr = res[el] # [1, 3, 10]
        a = 0
        for i in range(0, len(arr)-1):
            if (arr[i+1] - arr[i]) > a:
                a = arr[i+1] - arr[i]
        res[el] = a
    m = 0
    user = ''
    for i in res.keys():
        if res[i] > m:
            m = res[i]
            user = i
    return f'{res}, Пользователь с самым большим перерывом: {user}'


print(count_messages())
print('----------------------------------------')
print(different_and_frequent_words())
print('----------------------------------------')
print(find_biggest_dict())
print('----------------------------------------')
print(general_words())
print('----------------------------------------')
print(break_before_sms())