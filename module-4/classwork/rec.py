import random
# def factorial(i):
#     if i == 1:
#         return 1
#     else:
#         return i * factorial(i-1)

# print(factorial(5))

# def pow(x, y):
#     if y == 1:
#         return x 
#     else:
#         return x * pow(x, y-1)
    
# print(pow(2, 4))

# def summ(a, b):
#     if a == b:
#         return a
#     else:
#         return a + summ(a+1, b)
    
# print(summ(2,6))
# def draw(n):
#     if n == 1:
#         return '*'
#     else:
#         return "*" + draw(n-1)
    
# print(draw(6))
best_sum = None
best_index = 0
arr = [random.randint(-50, 50) for x in range(100)]
def summ(i):
    global best_sum, best_index
    if i + 10 > len(arr):
        return best_index
    else:
        if best_sum == None or sum(arr[i:i+10]) < best_sum:
            best_sum = sum(arr[i:i+10])
            best_index = i

    summ(i+1)
    

print(arr)
print(summ(0))
print(arr[best_index:best_index+10])

