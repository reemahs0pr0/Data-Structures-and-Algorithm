import random
import heapq

def heapsort(arr):
    length = len(arr)
    for i in range(length):
        if i==0:
            heapq.heapify(arr)
            arr.append(heapq.heappop(arr))
        else:
            x = arr[:-i]
            heapq.heapify(x)
            elem = heapq.heappop(x)
            arr.append(elem)
            arr.remove(elem)

if __name__ == '__main__':
    arr = []
    for i in range(10):
        arr.append(random.randint(-99,99))
    print(arr)
    heapsort(arr)
    print(arr)