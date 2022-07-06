class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class ll:
    def __init__(self):
        self.head=None

    def push(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        currnode=self.head
        while currnode.next is not None:
            currnode=currnode.next
        currnode.next=newnode

    def getmiddle(self):
        if (self.head == None):
            return self.head
        slow = self.head
        fast = self.head
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        print("\nMiddle element is : ",slow.data)

    def printlist(self):
        if self.head is None:
            print(' ')
            return
        currnode=self.head
        while currnode:
            print(currnode.data,end=' ')
            currnode=currnode.next
        print(' ')

l=ll()
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.printlist()
l.getmiddle()