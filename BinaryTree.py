class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def insert_right(self, val):
        if self.right is None:
            self.right = Node(val)
        else:
            self.right.insert_right(val)
    
    def insert_left(self, val):
        if self.left is None:
            self.left = Node(val)
        else:
            self.left.insert_left(val)

def serialize(node):
    if 'serial' not in locals():
        serial = ''
    if node.left:
        serial += serialize(node.left)
    serial += node.val + ' '
    if node.right:
        serial += serialize(node.right)
    return serial

def deserialize(serial):
    arr = sort(serial)
    root = Node('root')
    for i in range(len(arr)):
        if (arr[i] == 'root'):
            continue
        val_arr = arr[i].split('.')
        if (len(val_arr) == 1 and val_arr[0] == 'left'):
            root.insert_left('left')
        elif (len(val_arr) == 1 and val_arr[0] == 'right'):
            root.insert_right('right')
        else:
            base = root
            for j in range(len(val_arr)-1):
                if (val_arr[j] == 'left'):
                    root = root.left
                else:
                    root = root.right
                if (j == len(val_arr)-2):
                    if (val_arr[len(val_arr)-1] == 'left'):
                        root.insert_left(arr[i])
                    else:
                        root.insert_right(arr[i])
                    root = base
    return root

def sort(serial):
    arr = serial.split()
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if len(arr[j]) > len(arr[j+1]):
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr

node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right', Node('right.left'), Node('right.right')))
print(serialize(node))
assert deserialize(serialize(node)).left.left.val == 'left.left'