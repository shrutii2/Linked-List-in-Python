
class Node:
	def __init__(self, next = None,
					prev = None, data = None):
		self.next = next # reference to next node in DLL
		self.prev = prev # reference to previous node in DLL
		self.data = data

def push(head, new_data):
	new_node = Node(data = new_data)
	new_node.next = head
	new_node.prev = None
	if head is not None:
		head.prev = new_node
	head = new_node
	return head

def printList(head):
	node = head
	print("Given linked list")
	while(node is not None):
		print(node.data, end = " "),
		last = node
		node = node.next
	
def rotate(start, N):
	if N == 0 :
		return
	current = start
	count = 1
	while count < N and current != None :
		current = current.next
		count += 1
	if current == None :
		return
	NthNode = current
	while current.next != None :
		current = current.next
	current.next = start
	start.prev = current
	start = NthNode.next
	start.prev = None
	NthNode.next = None
	return start

# Driver Code
if __name__ == "__main__":
	head = None
	head = push(head, 'e')
	head = push(head, 'd')
	head = push(head, 'c')
	head = push(head, 'b')
	head = push(head, 'a')
	printList(head)
	print("\n")
	N = 2
	head = rotate(head, N)
	printList(head)

