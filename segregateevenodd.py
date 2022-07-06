# t(n)=O(n)

head=None
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def segregate():
    global head
    evenstart=None         # starting node of list having even values
    evenend=None           # Ending node of even values list.
    oddstart=None          # Starting node of odd values list.
    oddend=None            # Ending node of odd values list.
    currnode=head          # nodes to traverse list      
    while currnode!=None:
        val=currnode.data
        if (val%2==0):      #if current value is even,then add to list 
            if(evenstart==None):
                evenstart=currnode
                evenend=evenstart
            else:
                evenend.next=currnode
                evenend=evenend.next
        else:                #If curr value is odd    
            if(oddstart==None):
                oddstart=currnode
                oddend=oddstart
            else:
                oddend.next=currnode
                oddend=oddend.next
        currnode=currnode.next     # move head pointer one step in fwd direction
    if(oddstart==None or evenstart==None):
        return
    evenend.next=oddstart          # Add odd list after even list.
    oddend.next=None
    head=evenstart                 # Modify head pointer to starting of even list.

def push(newdata):
    global head
    newnode=node(newdata)
    newnode.next=head
    head=newnode

def printList():
    global head
    Node=head
    while(Node!=None):
        print(Node.data,end=' ')
        Node=Node.next
    print()

push(11)
push(10)
push(9)
push(6)
push(4)
push(1)
push(0)
print("Original Linked list")
printList()
segregate()
print("Modified Linked list")
printList()
