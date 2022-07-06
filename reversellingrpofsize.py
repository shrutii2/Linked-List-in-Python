# T(n)= O(n)           S(n)=O(n/k)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def reverse(self,head,k):
        if head== None:
            return None
        current=head
        next=None
        prev=None
        count=0

        while (current is not None and count<k):
            next=current.next
            current.next=prev
            prev=current
            current=next
            count+=1

        if next is not None:
            head.next=self.reverse(next,k)

        return prev

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next


ll=LL()
ll.push(9)
ll.push(8)
ll.push(7)
ll.push(6)
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
print("Given Linked list: ")
ll.printList()
ll.head=ll.reverse(ll.head,3)
print("\nReverse linked list: ")
ll.printList()