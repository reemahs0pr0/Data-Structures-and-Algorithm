def knapsack(n, W):
    if memo[n][W] != None:
        return memo[n][W]
    if n == 0 or W == 0:
        result = 0
    elif w[n] > W:
        result = knapsack(n-1, W)
    else:
        temp1 = v[n] + knapsack(n-1, W-w[n])
        temp2 = knapsack(n-1, W)
        result = max(temp1, temp2)
    memo[n][W] = result
    return result

import random

W = 20
v = [None]
w = [None]

for i in range(5):
    v.append(random.randint(1,20)*10)
    w.append(random.randint(1,20))

n = len(v)-1        
print("Values: " + str(v[1:]))
print("Weights: " + str(w[1:]))
print("Capacity: " + str(W))

memo = [[None] * (W+1)] * (n+1)
print(knapsack(n, W))