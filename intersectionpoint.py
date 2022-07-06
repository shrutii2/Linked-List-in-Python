# Y formation

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def intersectionpoint(a,b):
    h=set()
    while a!=None:
        h.add(a)
        a=a.next
    while b!=None:
        if b in h:
            return b
        b=b.next

    return None


def printlist(node):
    while(node!=None):
        print(node.data,end=' ')
        node=node.next

# list 1
a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)
a.next.next.next.next = Node(5)
a.next.next.next.next.next = Node(6)
a.next.next.next.next.next.next = Node(7)

# list 2
b = Node(10)
b.next = Node(9)
b.next.next = Node(8)
b.next.next.next = a.next.next.next

printlist(a)
print(" ")
printlist(b)
print("\nIntersection point is:  ")
print(intersectionpoint(a, b).data)