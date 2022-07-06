#  Time Complexity: O(N*Log(N))       Auxiliary Space: O(N)


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class node:
    def __init(self):
        self.data=0
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

# merge two sort linked list
    def sortedmerge(self,a,b):
        
        if a==None:
            return b
        if b==None:
            return a
        res=None
        if a.data<=b.data:
            res=a
            res.next=self.sortedmerge(a.next,b)
        else:
            res=b
            res.next=self.sortedmerge(a,b.next)
        
        return res

    def mergesort(self,h):
        if h==None or h.next==None:
            return h
        middle=self.getmiddle(h)
        nexttomiddle=middle.next
        middle.next=None
        left=self.mergesort(h)
        right=self.mergesort(nexttomiddle)
        sortedlist=self.sortedmerge(left,right)
        return sortedlist

    def getmiddle(self,head):
        if (head == None):
            return head
        slow = head
        fast = head
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def printlist(self,head):
        if self.head is None:
            print(' ')
            return
        n=self.head        #n=currentnode
        while n:
            print(n.data,end=' ')
            n=n.next
        print(' ')

# merging k ll in sorted manner - T(n)=O(nklogk)  S(n)=O(k)
def sortedmerge(a,b):
        res=None
        if a==None:
            return b
        if b==None:
            return a
        if a.data<=b.data:
            res=a
            res.next=sortedmerge(a.next,b)
        else:
            res=b
            res.next=sortedmerge(a,b.next)
        return res

def mergeklist(arr,last):
    while(last!=0):
        i=0
        j=last
        while(i<j):
            arr[i]=sortedmerge(arr[i],arr[j])
            i+=1
            j-=1
            if (i>=j):
                last=j
    return arr[0]

# merge point of two node.
def findMergeNode(head1, head2):
    p1 = head1
    p2 = head2
    len1 = len2 = 0
    while p1:
        len1 += 1
        p1 = p1.next
    while p2:
        len2 += 1
        p2 = p2.next
    if len1 > len2:
        for i in range(len1 - len2):
            head1 = head1.next
    else:
        for i in range(len2 - len1):
            head2 = head2.next
    while head1 and head2:
        if head1 == head2:
            return head1.data
        head1 = head1.next
        head2 = head2.next 

def printList(node):
    while (node != None):
        print(node.data, end = ' ')
        node = node.next

l=ll()
# l.push(15)
# l.push(10)
# l.push(5)
# l.push(20)
# l.push(3)
# l.push(2)
# l.head=l.mergesort(l.head)
# print('sorted merge list is: ')
# l.printlist(l.head)
a=l.push(5)
a=l.push(6)
b=l.push(4)
print(sortedmerge(a,b))
# l.head=l.sortedmerge(a,b)
# l.printlist(l.head)


def newNode(data):
    temp=node()
    temp.data=data
    temp.next=None
    return temp

# for merging k sortedlllist:
k=3 #no. of ll
n=4 #no. of elements in ll
arr = [0 for i in range(k)]

arr[0] = newNode(1)
arr[0].next = newNode(3)
arr[0].next.next = newNode(5)
arr[0].next.next.next = newNode(7)

arr[1] = newNode(2)
arr[1].next = newNode(4)
arr[1].next.next = newNode(6)
arr[1].next.next.next = newNode(8)

arr[2] = newNode(0)
arr[2].next = newNode(9)
arr[2].next.next = newNode(10)
arr[2].next.next.next = newNode(11)

# Merge all lists
head = mergeklist(arr, k - 1)
print("\nAfter merging k list: ")
printList(head)


