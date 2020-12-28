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
    
def num_ways_memoized(feet, memo):
    if feet in range(2):
        return 1
    else:
        if memo[feet] != None:
            return memo[feet]
        else:
            memo[feet] = 0
            memo[feet] = num_ways_memoized(feet-1, memo) + \
                        num_ways_memoized(feet-2, memo)
            return memo[feet]

import time
import matplotlib.pyplot as plt
import numpy as np

n = np.arange(0, 100)
bu_time = []
r_time = []
memo_time = []

for num in n:
    start1 = time.time()
    num_ways_bottom_up(num)
    bu_time.append(time.time() - start1)
    
    if num <= 20:
        start2 = time.time()
        num_ways_recursion(num)
        r_time.append(time.time() - start2)
    else:
        r_time.append(None)
    
    memo = [None] * (num+1)
    start3 = time.time()
    num_ways_memoized(num, memo)
    memo_time.append(time.time() - start3)
    
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(n, bu_time, color='red', linewidth=1, marker='o', label='bottom_up')
ax.plot(n, r_time, color='green', linewidth=1, marker='o', label='recursion')
ax.plot(n, memo_time, color='blue', linewidth=1, marker='o', label='memoized')
plt.legend(loc='upper right')
ax.set(title='Feet', ylabel='Time')
plt.show()