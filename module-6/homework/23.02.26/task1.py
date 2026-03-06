arr = [6,2,5,3,4,1]
pivot = len(arr) // 3
if sum(arr) / len(arr) > 0:
    seq_1 = arr[:pivot*2]
    seq_2 = arr[pivot*2:]
else:
    seq_1 = arr[:pivot]
    seq_2 = arr[pivot:]

seq_2.reverse()
seq_1.sort()
print(seq_1 + seq_2)
