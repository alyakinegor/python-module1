obj = {
    "Яо Мин": 229,
    "Карим Абдул-Джаббар": 218,
    "Уилт Чемберлен": 216,
    "Шакил О’Нил": 216,
    "Хаким Оладжьювон": 213,
    "Ларри Бёрд": 206,
    "Мэджик Джонсон": 206,
    "Леброн Джеймс": 206,
    "Коби Брайант": 198,
    "Майкл Джордан": 198
}
def add(key, value):
    obj[key] = value
def delete(key):
    del obj[key]

def search(key):
    return obj[key]

def swap_value(key, newVal):
    obj[key] = newVal

