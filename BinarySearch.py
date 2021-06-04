arr = [-2, 3, 4, 7, 8, 9, 11, 13]
target = 8
left = 0
right = len(arr) - 1
while (left <= right):
    middle = int((left + right) / 2)
    if (arr[middle] == target):
        print(middle)
        break
    elif (arr[middle] < target):
        left = middle + 1
    elif (arr[middle] > target):
        right = middle - 1
if (left > right):
    print("Target not in array")