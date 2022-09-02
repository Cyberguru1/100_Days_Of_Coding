#circular single linked list
# written by cyberguru1
# @2022 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLLk():
    def __init__(self):
        self.head = None
        self.tail = None
        self.NoElement = 0
    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next

    #adding element with pos to the list
    def addNode(self, data, pos):
        newdata = Node(data)
        #checking if its the first time adding data
        if self.head == None:
            self.head = newdata
            newdata.prev = None
            newdata.next = None
            self.tail = newdata
        #if position is the beginning, that is head
        #time complexity O(1) 
        elif pos == 0:
            newdata.next = self.head
            self.head.prev = newdata
            self.head = newdata

        #checking if position is at the end of the list 
        #time complexity O(1) {since we have tail}
        elif pos == 1:
            self.tail.next = newdata
            newdata.prev = self.tail
            self.tail = newdata

        #adding element inbetween the list 
        #time complexity O(N){due to looping through each element of the list}
        else:
            counter = 0
            pointer = self.head
            while counter < pos -1:
                pointer = pointer.next
                counter += 1
            nextnode = pointer.next
            pointer.next = newdata
            newdata.prev = pointer
            newdata.next = nextnode
            nextnode.prev = newdata
        self.NoElement += 1

    #traversing the list in forward manner starting from the head
    def traverse_forward(self):
        pointer = self.head
        while pointer:
            yield pointer.data
            pointer = pointer.next
        print(f'in forward order with {self.NoElement} elements')

    #traversing the list in reverse manner starting from the tail
    def traverse_reverse(self):
        pointer = self.tail
        while pointer:
            yield pointer.data
            pointer = pointer.prev
        print(f'in reverse order with {self.NoElement} elements')

    def deltenode(self, pos):
        if self.head == None : print("list is empty")
        if pos == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

        elif pos == 1:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None

            else:
                self.tail.prev.next = None
                self.tail = self.tail.prev  

        else:
            tempnode = self.head
            counter = 0
            while counter < pos - 1:
                tempnode = tempnode.next
                counter += 1

            delnode = tempnode.next
            tempnode.next = delnode.next
            delnode.next.prev = tempnode

    def searchNode(self, nodedata):
        if self.head == None : print("Double linked list is empty")
        if self.head.data == nodedata:
            return(nodedata)
        elif self.tail.data == nodedata:
            return(nodedata)
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.data == nodedata:
                    return(nodedata)
                tempnode = tempnode.next
        return "does not exsist in the list"
        
              



Dll = DoubleLLk()
Dll.addNode(1,1)
Dll.addNode(1,0)
Dll.addNode(2,1)
Dll.addNode(3,0)
Dll.addNode(4,2)



print(' <=> '.join([str(node) for  node in Dll.traverse_forward()]))

print(' <=> '.join([str(node) for node in Dll.traverse_reverse()]))
Dll.deltenode(1)
print([node.data for node in Dll])
print(Dll.searchNode(4))
