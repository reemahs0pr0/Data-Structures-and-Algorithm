import random
import time
from Quicksort import quicksort
from Selectionsort import selectionsort
from Bubblesort import bubblesort
from Mergesort import mergesort
from Insertionsort import insertionsort
from Shellsort import shellsort
from Heapsort import heapsort


arr1 = []
for i in range(9999):
    arr1.append(random.randint(-99,99))

arr2 = arr1.copy()
arr3 = arr1.copy()
arr4 = arr1.copy()
arr5 = arr1.copy()
arr6 = arr1.copy()
arr7 = arr1.copy()
arr8 = arr1.copy()

start = time.time()
quicksort(arr1, 0, len(arr1)-1)
print("Quick Sort time: %ss" % (time.time() - start))

start = time.time()
shellsort(arr2)
print("Shell Sort time: %ss" % (time.time() - start))

start = time.time()
mergesort(arr3)
print("Merge Sort time: %ss" % (time.time() - start))

start = time.time()
heapsort(arr4)
print("Heap Sort time: %ss" % (time.time() - start))

start = time.time()
selectionsort(arr5)
print("Selection Sort time: %ss" % (time.time() - start))

start = time.time()
insertionsort(arr6)
print("Insertion Sort time: %ss" % (time.time() - start))

start = time.time()
bubblesort(arr7)
print("Bubble Sort time: %ss" % (time.time() - start))

start = time.time()
arr8.sort()
print("Python Sort time: %ss" % (time.time() - start))