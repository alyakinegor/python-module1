nums = [2, 7, 11, 15]
target = 18
def summ(nums):
    for el in nums:
        for i in nums:
            if el + i == target:
                print(nums.index(el))
                print(nums.index(i))
                return
summ(nums)