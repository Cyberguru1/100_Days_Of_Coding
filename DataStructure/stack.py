class Node:

	def __init__(self, value = None):
		'''Node class with value input'''
		self.value = value
		self. next = None

class linkedlist:
	
	''' linked list class'''


	def __init__(self, head):
    self.head = None


class stack:
	
	'''Stack class'''

	def __init__(self):
		self.linkedlist = linkedlist()


	def isEmpty(self):
		
		''' checks if the stack is empty'''
		if self.linkedlist.head == None :
			return True
			
		else:
			False 

	def push(self, value):
		
		''' Adds an element in to the stack'''
		newData = Node(value)

		if self.linkedlist.head == None :
			newdata.next = self.linkedlist.head
			self.linkedlist.head = newData

		else:
			newData.next = self.linkedlist.
