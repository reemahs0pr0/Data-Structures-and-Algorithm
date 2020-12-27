import random

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp

if __name__ == '__main__':
    arr = []
    for i in range(10):
        arr.append(random.randint(-99,99))
    print(arr)
    bubblesort(arr)
    print(arr)