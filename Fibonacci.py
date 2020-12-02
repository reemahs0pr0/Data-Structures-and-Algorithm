def num_ways_bottom_up(feet):
    if feet in range(2):
        return 1
    else:
        num1 = 1
        num2 = 1
        for i in range(2, feet+1):
            temp = num2
            num2 += num1
            num1 = temp
        return num2
    
def num_ways_recursion(feet):
    if feet in range(2):
        return 1
    else:
        return num_ways_recursion(feet-1) + num_ways_recursion(feet-2)

import time
import matplotlib.pyplot as plt
import numpy as np

n = np.arange(0, 34)
bu_time = []
r_time = []

for num in n:
    start1 = time.time()
    num_ways_bottom_up(num)
    bu_time.append(time.time() - start1)
    start2 = time.time()
    num_ways_recursion(num)
    r_time.append(time.time() - start2)
    
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(n, bu_time, color='red', linewidth=1, marker='o', label='bottom_up')
ax.plot(n, r_time, color='green', linewidth=1, marker='o', label='recursion')
plt.legend(loc='upper left')
ax.set(title='Feet', ylabel='Time')
plt.show()