# T(n)=O(n)             S(n)=O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        ptr1 = Node(data)
        temp = self.head
        ptr1.next = self.head
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next 
            temp.next = ptr1
        else:
            ptr1.next = ptr1 # For the first node
        self.head = ptr1 

    def printList(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print ("%d" %(temp.data),end=' ')
                temp = temp.next
                if (temp == self.head):
                    break 

    def splitList(self, head1, head2):
        slow_ptr = self.head 
        fast_ptr = self.head
        if self.head is None:
            return 
          
        # If there are odd nodes in the circular list then
        # fast_ptr->next becomes head and 
        # for even nodes fast_ptr->next->next becomes head
        while(fast_ptr.next != self.head and 
            fast_ptr.next.next != self.head ):
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        # If there are even elements in list then
        # move fast_ptr
        if fast_ptr.next.next == self.head:
            fast_ptr = fast_ptr.next
        # Set the head pointer of first half
        head1.head = self.head
        # Set the head pointer of second half
        if self.head.next != self.head:
            head2.head = slow_ptr.next
        # Make second half circular
        fast_ptr.next = slow_ptr.next
        # Make first half circular
        slow_ptr.next = self.head


# Initialize lists as empty
head = CircularLinkedList() 
head1 = CircularLinkedList()
head2 = CircularLinkedList()
head.push(12)
head.push(56)
head.push(4)
head.push(2)
head.push(11)
print ("Original Circular Linked List")
head.printList()
# Split the list 
head.splitList(head1 , head2)
print ("\nFirst Circular Linked List")
head1.printList()
print ("\nSecond Circular Linked List")
head2.printList()