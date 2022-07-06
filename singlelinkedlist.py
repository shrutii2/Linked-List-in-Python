'''Time Complexity
	    Worst Case	Average Case
Search	    O(n)	O(n)
Insert	    O(1)	O(1)
Deletion	O(1)	O(1)
Auxiliary Space:  O(n)'''



class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class singleLinkedlist:
	def __init__(self):
		self.head=None

	def print_list(self):
		if self.head is None:
			print("List has no element")
			return
		else:
			temp=self.head
			while temp is not None:
				print(temp.data,'')
				temp=temp.next                            #contain reference to next node
#when it comes to last node reference node becomes None and loop terminates
	
	def insert_at_start(self,data):
		new_node = Node(data)
		new_node.next=self.head
		self.head=new_node

	def insert_at_end(self,data):
		new_node=Node(data)
		if self.head is None:
			self.head=new_node
		else:
			n=self.head
			while n.next is not None:
				n=n.next
			n.next = new_node

	def insert_after_data(self,x,data):
		n = self.head
		print(n.next)
		while n is not None:
			if n.data == x:
				break
			n = n.next
		if n is None:
			print("data not in the list")
		else:
			new_node = Node(data)
			new_node.next = n.next
			n.next = new_node

	def insert_before_data(self,x,data):
		if self.head is None:
			print("List has no data")
			return
		if x==self.head.data:
			new_node=Node(data)
			new_node.next=self.head
			self.head=new_node
			return
		n=self.head
		print(n.next)
		while n.next is not None:
			if n.next.data==x:
				break
			n=n.next
		if n.next is None:
			print("data not in list")
		else:
			new_node=Node(data)
			new_node.next=n.next
			n.next=new_node

	def insert_at_index (self, index, data):
		newnode=Node(data)
		if index ==0:
			if self.head==None:
				return newnode
			else:
				newnode.next=self.head
				return newnode
		else:
			node=self.head
			i=1
			while node.next!=None:
				nextnode=node.next
				if index==i:
					node.next=newnode
					newnode.next=nextnode
					return self.head
				node=node.next
				i+=1
			node.next=newnode
		return self.head 

	def get_count(self):
		if self.head is None:
			return 0
		count=0
		n=self.head
		while n is not None:
			count+=1
			n=n.next
		return count

	def search_data(self,x):
		if self.head is None:
			print("List has no data")
			return
		n=self.head
		while n is not None:
			if n.data==x:
				print("data found")
				return True
			n=n.next
		print("data not found")
		return False

	def make_new_list(self):
		nums=int(input("How many nodes do you want to create: "))
		if nums==0:
			return
		for i in range(nums):
			value=int(input("Enter value for node: "))
			self.insert_at_end(value)

	def delete_at_start(self):
		if self.head is None:
			print("List has no element to delete")
			return
		self.head=self.head.next

	def delete_at_end(self):
		if self.head is None:
			print("List has no element to delete")
			return
		n=self.head
		while n.next.next is not None:
			n=n.next
		n.next=None

	def delete_element_by_value(self,x):
		if self.head is None:
			print("List has no element to delete")
			return
		if self.head.data ==x:
			self.head=self.head.next
			return
		n=self.head
		while n.next is not None:
			if n.next.data == x:
				break
			n=n.next
		if n.next is None:
			print("data not found in list")
		else:
			n.next=n.next.next

	def delete_node_by_position(self,position):
		if position==0:
			return self.head.next
		current=self.head
		for i in range(position-1):
			current=current.next
		current.next=current.next.next
		
		return self.head


	def reverse_slinkedlist(self):
		prev=None
		n=self.head
		while n is not None:
			next=n.next
			n.next=prev
			prev=n
			n=next
			self.head=prev
		return self.head

	def bub_sort_datachange(self):              #bubblesort for exchanging data
		end = None
		while end != self.head:
			p = self.head
			while p.next != end:
				q = p.next
				if p.data > q.data:
					p.data , q.data = q.data , p.data
				p = p.next
			end = p

	def bub_sort_linkchange(self):               #bubblesort for modifyinglinks
		end=None
		while end !=self.head:
			r=p=self.head
			while p.next!=end:
				q=p.next
				if p.data>q.data:
					p.next=q.next
					q.next=p
					if p!=self.head:
						r.next=q
					else:
						self.head=q
					p,q=q,p
				r=p
				p=p.next
			end=p

	def merge_helper(self, list2):                      #MERGING TWO SORTED LIST
		merged_list = singleLinkedlist()
		merged_list.head = self.merge_by_newlist(self.head,list2.head)
		return merged_list
		
	def merge_by_newlist(self, p, q):
		if p.data <= q.data:
			head = Node(p.data)
			p = p.next
		else:
			head = Node(q.data)
			q = q.next	
		em = head
		while p is not None and q is not None:
			if p.data <= q.data:
				em.next = Node(p.data)
				p = p.next
			else:
				em.next = Node(q.data)
				q = q.next
			em = em.next
		while p is not None:
			em.next = Node(p.data)
			p = p.next
			em = em.next
		while q is not None:
			em.next = Node(q.data)
			q = q.next
			em = em.next
		
		return head


	def movetofront(self):
		temp=self.head
		second_last=None

		if not temp or not temp.next:
			return
		while temp and temp.next:
			second_last=temp
			temp=temp.next
		second_last.next=None
		temp.next=self.head
		self.head=temp

	def getNode(self, positionFromTail):
		if not self.head:
			return None
		if not self.head.next:
			return self.head.data
		lst_len = 0
		ptr =self.head
		while ptr.next:
			lst_len += 1
			ptr = ptr.next
		while lst_len > positionFromTail:
			self.head = self.head.next
			lst_len -= 1
		return self.head.data

	def compare_lists(self, llist2):
		llist2=llist2.head
		if self.head is None and llist2 is None:
			return 0
		else:
			node1=self.head
			node2=llist2
			while node1 and node2 :
				if self.head.data != llist2.data:
					return 0
				node1=node1.next
				node2=node2.next
			if node1 is None and node2 is None:
				return 1
			else:
				return 0	

def reverseprint(head):      #print in reverse
    # Write your code here
    if head==None:
        return
    reverseprint(head.next)
    print(head.data)




S_linkedlist=singleLinkedlist()
# S_linkedlist.insert_at_end(7)
# S_linkedlist.insert_at_end(1)
# S_linkedlist.insert_at_end(6)
# S_linkedlist.insert_at_start(8)
# lets add new data 16 after 10:
# S_linkedlist.insert_after_data(6,80)
# insert another data before 16 ie 20
# S_linkedlist.insert_before_data(1,10)
# S_linkedlist.insert_at_index(3,45)
# S_linkedlist.print_list()
# print(" ")
# S_linkedlist.movetofront()
# S_linkedlist.print_list()
# S_linkedlist.get_count()
# S_linkedlist.print_list()
# S_linkedlist.search_data(5)
# S_linkedlist.make_new_list()
# S_linkedlist.print_list()
# S_linkedlist.delete_node_by_position(2)
# S_linkedlist.print_list()
# S_linkedlist.delete_at_start()
# S_linkedlist.delete_at_end()
# S_linkedlist.delete_element_by_value(10)
# S_linkedlist.print_list()
# S_linkedlist.reverse_slinkedlist()
# S_linkedlist.print_list()
# S_linkedlist.bub_sort_datachange()
# S_linkedlist.print_list()
# S_linkedlist.bub_sort_linkchange()
# S_linkedlist.print_list()

# merging twosortedlist
# S_linkedlist.make_new_list()
# Sec_linkedlist=singleLinkedlist()
# Sec_linkedlist.make_new_list()
# S_linkedlist.bub_sort_datachange()
# Sec_linkedlist.bub_sort_datachange()
# RESult=S_linkedlist.merge_helper(Sec_linkedlist)
# RESult.print_list()

# comparing two linkedlist
# llist2=singleLinkedlist()
# S_linkedlist.insert_at_start(1) 
# S_linkedlist.insert_at_start(2) 
# S_linkedlist.insert_at_start(3) 
# S_linkedlist.insert_at_start(4)
# llist2.insert_at_start(1) 
# llist2.insert_at_start(2) 
# llist2.insert_at_start(3)
# llist2.insert_at_start(4)
# print(S_linkedlist.compare_lists(llist2))

# printing nth node from end of a ll
# S_linkedlist.insert_at_start(20)
# S_linkedlist.insert_at_start(4)
# S_linkedlist.insert_at_start(15)
# S_linkedlist.insert_at_start(35)
# print(S_linkedlist.getNode(4))
