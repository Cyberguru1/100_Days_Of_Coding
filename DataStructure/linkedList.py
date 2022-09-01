#circular single linked list
# written by cyberguru1
# @2022 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class linkedlist():
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.NoElement = 0

    def  addNode(self, data, pos):
        Newdata = Node(data)
        if self.head == None:
            self.head = Node(data)
            self.tail = Node(data)
            

        elif pos == 0:
            Newdata.next = self.head
            self.head = Newdata
            
        
        elif pos == 1:
            temp = self.head
            while temp.next != None :
                temp = temp.next
            temp.next = Node(data)
        
        else:
            N = 0
            movin_pointer = self.head
            while (N < pos-1):
                N +=1
                movin_pointer = movin_pointer.next
    
            Nextnode= movin_pointer.next
            movin_pointer.next = Newdata
            Newdata.next = Nextnode
        self.NoElement +=1
    
    def deletnode(self, pos):
        if pos == 0:
            nextnode = self.head.next
            self.head = nextnode
        elif pos == 1:
            deln = self.head.next #ralf <(*__^)>
            self.head.next = deln.next
        else:
            N = 0
            iterator = self.head
            while (N < pos - 1):
                iterator = iterator.next
                N +=1
            iterator.next = iterator.next.next
        self.NoElement -= 1
            
    def reverse(self):
        itrate = self.head
        prevv = self.tail

        while itrate:
            currt = itrate
            nextnode = currt.next
            currt.next = prevv
            prevv = currt
            itrate = nextnode
        self.head = prevv

    def sort(self):
        while True:
            moving = 0
            itrate = 0
            pointer = self.head
            while itrate < self.NoElement - 1:
                if pointer.data > pointer.next.data:
                    temp = pointer.next.data
                    pointer.next.data = pointer.data
                    pointer.data = temp
                    moving += 1
                pointer = pointer.next
                itrate += 1 
            if moving == 0:
                break

    def display(self) -> None:
        pointer = self.head
        while pointer != None:
            print(pointer.data)
            pointer = pointer.next
        print(f"No of Element: {self.NoElement}")
        


llk = linkedlist()


llk.addNode(20, 1)
llk.addNode(30, 1)
llk.addNode(40, 1)
llk.addNode(11, 1)
llk.addNode(5,1)
#llk.deletnode(3)
llk.reverse()
#llk.sort()
llk.display()

