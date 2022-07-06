# T(N) = O(m+n)  S(N) = O(max(m,n))

class Node:
    def __init__(self):
        self.data= 0
        self.next= None

# recursion
def sortIntersect(a,b):
    if a==None or b==None:
        return None
    if (a.data<b.data):
        return sortIntersect(a.next,b)
    elif a.data>b.data:
        return sortIntersect(a,b.next)
    else:
        temp=Node()
        temp.data=a.data
        temp.next=sortIntersect(a.next,b.next)
        return temp

def push(head_ref, new_data):
    new_node = Node()
    new_node.data = new_data
    new_node.next = head_ref
    head_ref = new_node
    return head_ref

def printlist(node):
    while(node!=None):
        print(node.data,end=' ')
        node=node.next


a=None
b=None
intersect=None
a = push(a, 9)
a = push(a, 8)
a = push(a, 7)
a = push(a, 6)
a = push(a, 5)
a = push(a, 4)
a = push(a, 3)
b = push(b, 9)
b = push(b, 8)
b = push(b, 3)
b = push(b, 2)
intersect=sortIntersect(a,b)
print("\nLinkedlist containing intersection from a and b is: ")
printlist(intersect)