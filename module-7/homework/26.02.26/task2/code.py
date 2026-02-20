count_lines = 0
count_symbols = 0
count_vowels = 0
count_consonant = 0
vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxz"
with open('module-7/homework/26.02.26/task2/example.txt', 'r', encoding='utf-8') as f:
    for line in f.read().split('\n'):
        count_lines += 1
        for el in line:
            count_symbols += 1
            if el in vowels:
                count_vowels += 1
            elif el in consonants:
                count_consonant += 1

with open('module-7/homework/26.02.26/task2/statistic.log', 'w', encoding='utf-8') as r:
    r.write(f"""Количество строчек: {count_lines}
количество символов: {count_symbols}
количество гласных: {count_vowels}
количество согласных: {count_consonant}""")
    
