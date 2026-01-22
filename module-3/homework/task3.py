li1 = [1,2,3,4]
li2 = [3,4,5,6]
def outer_join(l1, l2):
    l3 = l1 + l2
    print(l3)

def distinct(l1, l2):
    l3 = l1 + l2
    print(list(set(l3)))

def inner_join(l1, l2):
    l3 = []
    for el in l1:
        if el in l2:
            l3.append(el)
    print(l3)

def special(l1, l2):
    l3 = []
    for el in l1:
        if el not in l2:
            l3.append(el)
    for el in l2:
        if el not in l1:
            l3.append(el)
    print(l3)

def minmax(l1, l2):
    l3 = []
    l3.append(min(l1))
    l3.append(max(l1))
    l3.append(min(l2))
    l3.append(max(l2))
    print(l3)

outer_join(li1, li2)
distinct(li1, li2)
inner_join(li1, li2)
special(li1, li2)
minmax(li1, li2)