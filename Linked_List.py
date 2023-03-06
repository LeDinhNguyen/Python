## Create a Linked List

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
class LinkedList:
	def __init(self):
		self.head = None

# create and assign value to node
one = Node(1)
two = Node(2)
three = Node(3)

# create linked list
linked_list = LinkedList()

linked_list.head = one
one.next = two
two.next = three

# print the linked list
while linked_list.head != None:
	print(linked_list.head.value)
	linked_list.head = linked_list.head.next
