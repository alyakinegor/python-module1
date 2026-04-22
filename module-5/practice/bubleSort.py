arr = [5,6,3,2,4,1,8]

def buble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swp = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swp = True
        if not swp:
            break 

buble_sort(arr)
print(arr)