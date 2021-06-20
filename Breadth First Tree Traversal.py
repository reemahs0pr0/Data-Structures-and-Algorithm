class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def printLevelOrder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while(len(queue) > 0):
        print (queue[0].val, end=" ")
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print ("Level Order Traversal of binary tree is -")
printLevelOrder(root)