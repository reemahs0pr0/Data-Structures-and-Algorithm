import random

def shellsort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while arr[j-gap] > temp and j >= gap:
                arr[j] = arr[j-gap]
                j = j - gap
            arr[j] = temp
        gap = gap // 2
        
if __name__ == '__main__':
    arr = []
    for i in range(10):
        arr.append(random.randint(-99,99))
    print(arr)
    shellsort(arr)
    print(arr)