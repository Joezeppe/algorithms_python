

class Node(object):
	def __init__(self, data=None, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev = prev


class DoublyLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0

	def append(self, data):
		""" Append an item to the list. """
		new_node = Node(data, None, None)
		if self.head is None:
			self.head = new_node
			self.tail = self.head
		else:
			new_node.prev = self.tail
			self.tail.next = new_node
			self.tail = new_node
			self.count += 1




