from typing import Any

class Node(object):
    def __init__(self, value = None) -> Any:
        self.value = value
        self.next = None
        self.prev = None

class CircularDLL(object):

    def __iter__(self):
        pointer = self.head
        while pointer:
            yield pointer.value
            if pointer.next == self.head:
                break
            pointer = pointer.next

    def CreateCDLL(self, value):
        newnode = Node(value)
        newnode.next = newnode
        newnode.prev = None
        self.head = newnode
        self.tail = newnode

    def insert(self, value, pos = None):
        newnode = Node(value)

        #check if this is the first time of adding data to the list
        if self.head == self.tail:
            self.head.next = newnode
            newnode.next = self.head
            newnode.prev = self.head
            self.tail = newnode

        else:
            if  pos == 0:
                newnode.next = self.head
                self.head.prev = newnode
                self.tail.next = newnode
                self.head = newnode

            elif pos == 1:
                self.tail.next = newnode
                newnode.prev = self.tail
                newnode.next = self.head
                self.tail = newnode

            else:
                counter = 0
                pointer = self.head
                while counter < pos -1:
                    pointer = pointer.next

                nextnode = pointer.next
                pointer.next = newnode
                newnode.prev = pointer
                newnode.next = nextnode
                nextnode.prev = newnode

    def traverse_Forward(self):
        pass
    def traverse_reverse(self):
        pass
    def DeleteNode(self):
        pass
    def reverse(self):
        pass

CDLL = CircularDLL()
CDLL.CreateCDLL(0)
CDLL.insert(1)
CDLL.insert(2, 0)
CDLL.insert(3, 0)
CDLL.insert(4, 0)
CDLL.insert(5, 0)
print([value for value in CDLL])