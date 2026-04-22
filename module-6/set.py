s = set([1,2,3])
# s1 = set('aaaabb')
# s2 = set((1,2,2,3))
# s3 = {x for x in range(5)}
# fr = {'apple', 'banana', 'orange'}
# fr.add('coconut')
# fr.update(['cherry', 'tomato'])
# fr.remove('apple')
# fr.discard('ice')
# fr.pop()
# print(fr)

s2 = {2,3,4,5,6}
# res = s | s2
# s |= s2
# print(res)
# print(s)
# print(s.union(s2))

# res = s.intersection(s2)
# res = s & s2
# s &= s2
# print(s)

# res = s2.difference(s)
# res = s2 - s
# print(res)

# res = s2.symmetric_difference(s)
# res = s ^ s2
# print(res)

print(3 in s)
print(4 not in s)
print(len(s))
print(sum(s))
print(min(s))
print(max(s))
print(list(x for x in s))