def upgrade_buble_sort(arr):
    for i in range(len(arr)):
        n = 0
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                n += 1
            if n == 0:
                return arr

    return arr

print(upgrade_buble_sort([9,6,5,3,1]))