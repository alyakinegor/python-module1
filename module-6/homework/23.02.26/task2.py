marks = list(map(int, input().strip().split()))
def rewrite_exam(idx, val):
    arr1 = marks[:idx]
    arr2 = marks[idx+1:]
    return arr1 + [val] + arr2

def check_for_grant():
    return sum(marks) / len(marks) >= 10.7

def sort_marks(dec=False):
    arr = sorted(marks)
    return list(reversed(arr)) if dec else  arr

print(sort_marks(dec=True))
