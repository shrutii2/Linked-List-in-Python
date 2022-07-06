
class Node:
	
	def __init__(self, data):
		
		self.data=data
		self.next=None
		self.prev=None


def countTriplets(head, x):

	ptr2=head
	count = 0
	um = dict()
	ptr = head
	while ptr!=None:
		um[ptr.data] = ptr
		ptr = ptr.next
	ptr1=head
	
	while ptr1!=None:
		ptr2 = ptr1.next
		while ptr2!=None:
			p_sum = ptr1.data + ptr2.data
			if ((x-p_sum) in um) and um[x - p_sum] != ptr1 and um[x - p_sum] != ptr2:
				count+=1
			ptr2 = ptr2.next
		ptr1 = ptr1.next
	return (count // 3)

def insert(head, data):
	temp = Node(data)
	if ((head) == None):
		(head) = temp
	else:
		temp.next = head
		(head).prev = temp
		(head) = temp
	return head
	
if __name__=='__main__':
	head = None
	# insert values in sorted order
	head = insert(head, 9)
	head = insert(head, 8)
	head = insert(head, 6)
	head = insert(head, 5)
	head = insert(head, 4)
	head = insert(head, 2)
	head = insert( head, 1)
	x = 17
	print("Count = "+ str(countTriplets(head, x)))
	
