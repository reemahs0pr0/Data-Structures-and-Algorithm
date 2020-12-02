class Node:
    def __init__(self, val, prev=None, nex=None):
        self.val = val
        self.prev = prev
        self.nex = nex
    
    def add(self, val):
        if self.nex is None:
            self.nex = Node(val, self)
        else:
            self.nex.add(val)
            
    def get(self, index, i=0):
        if i == index:
            return self
        else:
            i += 1
            return self.nex.get(index, i=i)
        
    def insert(self, val, index):
        linkedList.get(index).prev = Node(val, linkedList.get(index-1), 
                                          linkedList.get(index))
        linkedList.get(index-1).nex = Node(val, linkedList.get(index-1), 
                                           linkedList.get(index))
        
    def getLength(self, count=1):
        if self.nex:
            count += 1
            return self.nex.getLength(count=count)
        return count
    
    def remove(self, index):
        linkedList.get(index-1).nex = linkedList.get(index+1)
        linkedList.get(index).prev = linkedList.get(index-1)
        

linkedList = Node(1)
linkedList.add(2)
linkedList.add(3)
linkedList.add(4)
linkedList.add(5)
linkedList.add(6)
linkedList.add(7)
linkedList.add(8)
linkedList.add(9)
linkedList.add(10)
linkedList.insert(99, 5)
linkedList.insert(69, 3)
linkedList.insert(55, 10)
linkedList.remove(3)
linkedList.remove(5)
linkedList.remove(8)
print("Length: " + str(linkedList.getLength()))

for i in range(linkedList.getLength()):
    print(linkedList.get(i).val)
