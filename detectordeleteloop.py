# T(n) = O(n)   S(n)=O(1)
'''
1 - 2 - 3
    |   |           
    5 - 4
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class ll:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def detect(self):
        if (self.head==None):
            return False
        else:
            while(self.head!=None):
                if(self.head.data==-1):
                    return True
                else:
                    self.head.data=-1
                    self.head=self.head.next
            return False

    def detectandremoveloop(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        slow_p = self.head
        fast_p = self.head

        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:                        #if slowp and fastp meet at some point then there is loop
                slow_p = self.head
# Finding the beginning of the loop
                while (slow_p.next != fast_p.next):
                    slow_p = slow_p.next
                    fast_p = fast_p.next
                # Sinc fast.next is the looping point
                fast_p.next = None  # Remove loop
                
                return slow_p

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next


llist=ll()
# llist.push(1)
# llist.push(2)
# llist.push(3)
# llist.push(4)
# llist.push(5)
# llist.head.next.next.next.next.next=llist.head.next.next   #5 pointing to 3 to check for loop
# example2
llist.push(50)
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.head.next.next.next.next.next = llist.head.next.next
# llist.printlist()
if(llist.detect()):
    print ("Loop found")
else:
    print("No loop.")

llist.head = Node(50)
llist.head.next = Node(20)
llist.head.next.next = Node(15)
llist.head.next.next.next = Node(4)
llist.head.next.next.next.next = Node(10)
llist.head.next.next.next.next.next = llist.head.next.next.next

res=llist.detectandremoveloop()
print("Linked list after removing  loop : ",end=' ')
llist.printlist()
if (res == None):
    print("Loop does not exist")
else:
    print("\nLoop starting node is " + str(res.data))
