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
            pointer = pointer.next

    def __str__(self):
        Clist = [str(vaule) for value in CircularDLL]
        return " ,".join(clist)

    def CreateCDLL(self, value):
        newnode = Node(value)
        newnode.next = newnode
        newnode.prev = None
        self.head = newnode
        self.tail = newnode

    def insert(self, value, pos):
        pass