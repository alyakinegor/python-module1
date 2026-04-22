# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     less = [i for i in arr[1:] if i <= pivot]
#     greater = [i for i in arr[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([1,5,3,2]))

def func(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    less = [x for x in nums[1:] if x <= pivot]
    bigger = [x for x in nums[1:] if x > pivot]
    return func(less) + [pivot] + func(bigger)

nums = [0,0,1,3,2,5,6]
func(nums)
print(nums)