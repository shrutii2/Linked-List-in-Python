# T(n)=O(n) s(n)=O(1)
class Node:
	def __init__(self, x):
		self.data = x
		self.next = None
		self.prev = None

def pairSum(head, x):
	first = head         #for beginning of dll
	second = head        #at end of dll
	while (second.next != None):
		second = second.next
	found = False          #to track if we find pair or not
	while (first != second and second.next != first):   
		if ((first.data + second.data) == x):       #pair found
			found = True
			print("(", first.data, ",",
					second.data, ")")
			first = first.next                      #move first in fwd direction
			second = second.prev                    #move second in backward direction
		else:
			if ((first.data + second.data) < x):
				first = first.next
			else:
				second = second.prev
	if (found == False):
		print("No pair found")


def insert(head, data):                     #insert at beginning of dll
	temp = Node(data)
	if not head:
		head = temp
	else:
		temp.next = head
		head.prev = temp
		head = temp
	return head

# Driver code
if __name__ == '__main__':
	head = None
	head = insert(head, 9)
	head = insert(head, 8)
	head = insert(head, 6)
	head = insert(head, 5)
	head = insert(head, 4)
	head = insert(head, 2)
	head = insert(head, 1)
	x = 7

	pairSum(head, x)
