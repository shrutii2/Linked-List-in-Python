
class Node():
	def __init__(self,data):
		self.data = data
		self.right = None
		self.down = None

class LinkedList():
	def __init__(self):
		self.head = None

	def push(self,head_ref,data):
		new_node = Node(data)
		new_node.down = head_ref
		head_ref = new_node
		return head_ref

	def printList(self):
		temp = self.head
		while(temp != None):
			print(temp.data,end=" ")
			temp = temp.down
		print()

	# An utility function to merge two sorted linked lists
	def merge(self, a, b):
		if(a == None):
			return b
		if(b == None):
			return a
		result = None
		if (a.data < b.data):
			result = a
			result.down = self.merge(a.down,b)
		else:
			result = b
			result.down = self.merge(a,b.down)
		result.right = None
		return result

	def flatten(self, root):
		if(root == None or root.right == None):
			return root
		root.right = self.flatten(root.right)
		root = self.merge(root, root.right)
		return root


# Driver program to test above functions
L = LinkedList()
'''
Let us create the following linked list
			5 -> 10 -> 19 -> 28
			| |	 |	 |
			V V	 V	 V
			7 20 22 35
			|		 |	 |
			V		 V	 V
			8		 50 40
			|			 |
			V			 V
			30			 45
'''
L.head = L.push(L.head, 30)
L.head = L.push(L.head, 8)
L.head = L.push(L.head, 7)
L.head = L.push(L.head, 5)

L.head.right = L.push(L.head.right, 20)
L.head.right = L.push(L.head.right, 10)

L.head.right.right = L.push(L.head.right.right, 50)
L.head.right.right = L.push(L.head.right.right, 22)
L.head.right.right = L.push(L.head.right.right, 19)

L.head.right.right.right = L.push(L.head.right.right.right, 45)
L.head.right.right.right = L.push(L.head.right.right.right, 40)
L.head.right.right.right = L.push(L.head.right.right.right, 35)
L.head.right.right.right = L.push(L.head.right.right.right, 20)

# flatten the list
L.head = L.flatten(L.head)
L.printList()
