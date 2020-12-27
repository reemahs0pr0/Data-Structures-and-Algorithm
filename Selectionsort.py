import random

def selectionsort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

if __name__ == '__main__':
    arr = []
    for i in range(10):
        arr.append(random.randint(-99,99))
    print(arr)
    selectionsort(arr)
    print(arr)