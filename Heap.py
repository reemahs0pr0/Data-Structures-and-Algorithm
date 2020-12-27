import heapq as h

arr = [23, 45, 43, 56, 13, 69, 52, 64, 31, 45]

h.heapify(arr)
print(arr)

h.heappush(arr, 44)
print(arr)

h.heappop(arr)
print(arr)

h.heapreplace(arr, 104)
print(arr)