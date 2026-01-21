
s = '()()()[]'
obj = {
    ')': '(',
    ']': '[',
    '}': '{',

}
c = 0 
new = s
for el in s[:-1]:
    if el == obj.get(s[c+1]):
        new = new.replace(el, '', 1)
        new = new.replace(s[c+1], '', 1)
    c += 1
print(len(new)==0)