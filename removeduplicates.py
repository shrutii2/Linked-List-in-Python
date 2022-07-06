# t(n)= O(n) s(n)=O(1)     sort
# T(N)=O(N)  S(N)=O(N)     unsort


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class ll:
    def __init__(self):
        self.head=None

    def push(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        self.head=newnode

    # for sorting linkedlist
    def removeduplicate(self):
        temp=self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data==temp.next.data:
                new=temp.next.next
                temp.next=None
                temp.next=new
            else:
                temp=temp.next
        return self.head

    # for unsorted linked list
    def removeduplicates(self,head):
        if self.head is None or self.head.next is None:
            return head
        hash = set()
        current = head
        hash.add(self.head.data)
        while current.next is not None:
            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next
        return head


    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next

# sort
# llist=ll()
# llist.push(10)
# llist.push(11)
# llist.push(11)
# llist.push(11)
# llist.push(12)
# llist.push(12)
# print ("Created Linked List: ")
# llist.printList()
# print()
# print("Linked List after removing duplicate elements: ")
# llist.removeduplicate()
# llist.printList()

# unsort
llist = ll()
llist.head = Node(10)
second = Node(10)
third = Node(11)
fourth = Node(11)
fifth = Node(11)
sixth = Node(11)
seventh = Node(12)

    # Connecting second and third
llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = seventh

    # Printing data
print("Linked List before removing Duplicates.")
llist.printList()
llist.removeduplicates(llist.head)
print("\nLinked List after removing duplicates.")
llist.printList()