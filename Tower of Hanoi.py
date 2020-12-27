def move(n, source, target, spare):
    global step
    if n > 0:
        move(n-1, source, spare, target)
        target.append(source.pop())
        step += 1
        print("Move " + str(step))
        print("A: " + str(A), end=" ")
        print("B: " + str(B), end=" ")
        print("C: " + str(C), end="\n\n")
        move(n-1, spare, target, source)
        
A = []
B =[]
C = []
step = 0
pegs = 8

for i in range(pegs, 0, -1):
    A.append(i)
    
print("A: " + str(A), end=" ")
print("B: " + str(B), end=" ")
print("C: " + str(C), end="\n\n")

move(len(A), A, C, B)