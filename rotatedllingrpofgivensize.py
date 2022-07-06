
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def getNode(data):
	# allocating node
	new_node = Node(0)
	new_node.data = data
	new_node.next = new_node.prev = None
	return new_node

def push(head, new_node):
	new_node.prev = None
	new_node.next = head
	if ((head) != None):
		head.prev = new_node
	head = new_node
	return head

def printList(head):
	while (head):
		print(head.data, end=" ")
		head = head.next

def revListInGroupOfGivenSize(head, k):
	if head is None:
		return head
	st = head
	globprev, ans = None, None
	while (st != None):
		count = 1
		curr = st
		prev, next_node = None, None
		while (curr != None and count <= k):
			next_node = curr.next
			curr.prev = next_node
			curr.next = prev
			prev = curr
			curr = next_node
			count += 1
		if ans is None:
			ans = prev
			ans.prev = None
		if globprev is None:
			globprev = st
		else:
			globprev.next = prev
			prev.prev = globprev
			globprev = st
		st = curr
	return ans

head = None
head = push(head, getNode(2))
head = push(head, getNode(4))
head = push(head, getNode(8))
head = push(head, getNode(10))
print("Original list:", end=" ")
printList(head)
k = 2
head = revListInGroupOfGivenSize(head, k)
print("\nModified list:", end=" ")
printList(head)

