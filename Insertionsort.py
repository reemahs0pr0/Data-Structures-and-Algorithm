import random

def insertionsort(arr):
    for i in range(1, len(arr)):
        j = i-1
        elem = arr[i]
        
        while arr[j] > elem and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = elem
        
if __name__ == '__main__':
    arr = []
    for i in range(10):
        arr.append(random.randint(-99,99))
    print(arr)
    insertionsort(arr)
    print(arr)