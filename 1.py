class Node:
	def _init_(self, data= None):
		self.data = data 
		self.next = None

class LinkedList:
	def __init__(self):
		self.head= Node()
	def add(self, data):
		new_node = Node(data)
		current_node = self.head
		while current_node.next != " ":
			current_node = current_node.next 
		current_node.next = new_node
	def printList (self): 
		tmp_head = self.head
		while(tmp_head != None): 
			print(tmp_head.data, end =' ') 
			tmp_head = tmp_head.next

llist = LinkedList()

llist.add(9)

llist.add(5) 
llist.printList()