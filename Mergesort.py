import random

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

def merge(left, right):
    arr = []
    
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            arr.append(left[0])
            left.remove(left[0])
        else:
            arr.append(right[0])
            right.remove(right[0])
        
    if len(left) == 0:
        arr = arr + right
    else:
        arr = arr + left
    return arr

if __name__ == '__main__':
    arr = []
    for i in range(10):
        arr.append(random.randint(-99,99))
    print(arr)
    print(mergesort(arr))
