def Insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            print(key, j)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(Insertion_sort([5,7,6,3,4]))