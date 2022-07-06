# T(N)= O(NlogN)in avg case or best case , O(n^2)in worst case
#  S(N)=O(N) used because of recursion call stack

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

    def printlist(self,head):
        if self.head is None:
            print(' ')
            return
        currnode=self.head
        while currnode:
            print(currnode.data,end=' ')
            currnode=currnode.next
        print(' ')

    def partition(self,start,end):
        if (start == end or start == None or end == None):
            return start
        pivot_prev = start
        curr = start
        pivot = end.data
        while (start != end):
            if (start.data < pivot):
                pivot_prev = curr
                temp = curr.data
                curr.data = start.data
                start.data = temp
                curr = curr.next
            start = start.next
        temp = curr.data
        curr.data = pivot
        end.data = temp
        return pivot_prev

    def quicksort(self,start,end):
        if(start == None or start == end or start == end.next):
            return
        pivot_prev = self.partition(start, end)
        self.quicksort(start, pivot_prev)
        if(pivot_prev != None and pivot_prev == start):
            self.quicksort(pivot_prev.next, end)
        elif (pivot_prev != None and pivot_prev.next != None):
            self.quicksort(pivot_prev.next.next, end)

l=ll()
l.push(30)
l.push(3)
l.push(4)
l.push(20)
l.push(5)
n=l.head
while(n.next!=None):
    n=n.next
print("\nLinked list before sorting: ")
l.printlist(l.head)
l.quicksort(l.head,n)
print("\nLinked list after sorting : ")
l.printlist(l.head)