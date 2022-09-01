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

    #adding element with pos to the list
    def addNode(self, data, pos):
        newdata = Node(data)
        #checking if its the first time adding data
        if self.head == None:
            self.head = newdata
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

    #displaying the list in forward manner starting from the head
    def display_f(self):
        pointer = self.head
        while pointer:
            yield pointer.data
            pointer = pointer.next
        print(f'in forward order with {self.NoElement} elements')

    #displaying the list in reverse manner starting from the tail
    def display_r(self):
        pointer = self.tail
        while pointer:
            yield pointer.data
            pointer = pointer.prev
        print(f'in reverse order with {self.NoElement} elements')

Dll = DoubleLLk()
Dll.addNode(1,1)
Dll.addNode(1,0)
Dll.addNode(2,1)
Dll.addNode(3,0)
Dll.addNode(4,2)

print(' <=> '.join([str(node) for  node in Dll.display_f()]))

print(' <=> '.join([str(node) for node in Dll.display_r()]))
