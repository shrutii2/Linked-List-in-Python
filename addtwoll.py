
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

    def addtwolist(self,first,second):
        prev=None
        temp=None
        carry=0
        while(first is not None or second is not None):
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            Sum = carry + fdata + sdata
            carry=1 if Sum >=10 else 0
            Sum = Sum if Sum <10 else Sum%10
            temp=Node(Sum)
            if self.head is None:
                self.head=temp
            else:
                prev.next=temp
            prev=temp
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
            if carry > 0:
                temp.next = Node(carry)

    def printList(self,head):
        if self.head is None:
            print("List has no element")
            return
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,'')
                temp=temp.next

# Driver code
first = ll()
second = ll()

# Create first list
first.push(3)
first.push(6)
# first.push(9)
first.push(5)
# first.push(7)
print ("First List is ")
first.printList(first.head)
# Create second list
second.push(2)
second.push(4)
second.push(8)
print ("Second List is ")
second.printList(second.head)
# Add the two lists and see result
res = ll()
res.addtwolist(first.head,second.head)
print("Resultant list is ")
res.printList(res.head)