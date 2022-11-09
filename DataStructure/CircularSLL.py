#circular single linked list
# written by cyberguru1
# @2022 

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSLL():

    def __iter__(self):

        pointer = self.head
        while pointer:
            yield pointer.value
            if pointer.next == self.head:
                break
            pointer = pointer.next

    def createCSLL(self, value) -> str :
        node = Node(value)
        node.next = node            
        self.head = node
        self.tail = node
        print("circular single linked list created")

    def insertNode(self, data, pos):

        newdata = Node(data) #instanciate a new node

        if self.head == self.tail : #check if this the first time of adding data
            self.head.next = newdata 
            newdata.next = self.head
            self.tail = newdata
            

        else:

            if pos == 0 :   ##check if the position to insert node is at the beginnig
                newdata.next = self.head
                self.head = newdata
                self.tail.next = newdata

            elif pos == 1:  # check if position to insert node is at the end
                self.tail.next = newdata
                newdata.next = self.head
                self.tail = newdata

            else:              # else loop through the linked list to insert inbetween nodes
                pointer = self.head
                counter = 0
                while counter < pos -1:
                    pointer = pointer.next
                    counter +=1
                nextnode = pointer.next
                pointer.next = newdata
                newdata.next = nextnode

    def delnode(self, pos) :
        if pos == 0 :

            if self.head == self.tail: #check if the list is empty
                self.head = None
                self.tail = None
            else:                        #change the head node to next node
                self.head = self.head.next
                self.tail.next = self.head  #change the next node of the tail to updated head

        elif pos == 1:

            if self.head == self.tail: #check if the list is empty
                self.head = None
                self.tail = None

            else:
                pointer = self.head
                while pointer:
                    pointer = pointer.next    # loop through and find the node before the last node
                    if pointer.next == self.tail:
                        break
                deltednode = pointer.next
                pointer.next = deltednode.next  ## set the next node to head and set tail to pointer
                self.tail = pointer
        else:

            iterator = self.head
            count = 0
            while count < pos - 1:
                iterator = iterator.next
                count += 1

            delnod = iterator.next
            iterator.next = delnod.next
            

    def traverse(self) :
        pointer = self.head

        while pointer:
            print(pointer.value)
            pointer = pointer.next
            if pointer.next == self.head:
                break
                

CSLL = CircularSLL()

CSLL.createCSLL(0)
CSLL.insertNode(1, 1)
CSLL.insertNode(2, 1)
CSLL.insertNode(3, 0)
CSLL.insertNode(4, 1)
CSLL.insertNode(8, 1)
CSLL.insertNode(6, 3)
CSLL.insertNode(7, 2)
#CSLL.delnode(5)
#SLL.delnode(1)
#CSLL.delnode(0)

CSLL.traverse()
csll = [str(node) for node in CSLL]
print('_'*(len(csll)*3  - 2))
print('v'+' '*(len(csll)*3 - 4)+'v')
print('->'.join(csll))





    

