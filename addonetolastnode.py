# T(n) = O(N)          S(N) = O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def newNode(data):
    return Node(data)

def reverseList(head):
    prev=None
    n=head
    while n is not None:
        next=n.next
        n.next=prev
        prev=n
        n=next
        head=prev
    return head

def addOne(head):
    head = reverseList(head)   #reverse linkedlist and add 1 to head
    k = head
    carry = 0
    prev = None
    head.data += 1
    # update carry for next calculation
    while(head != None) and (head.data > 9 or carry > 0):
        prev = head
        head.data += carry
        carry = head.data // 10
        head.data = head.data % 10
        head = head.next
    if carry > 0:
        prev.next = Node(carry)
    # Reverse the modified list
    return reverseList(k)

#########ye push ko dekh re baba
def push(head,newdata):
    newnode=Node(newdata)
    newnode.next=head
    head=newnode     


def printList(head):
    if not head:
        return
    while(head):
        print("{}".format(head.data), end=" ")
        head = head.next

# Driver code
if __name__ == '__main__':
    head = newNode(1)
    head.next = newNode(9)
    head.next.next = newNode(9)
    head.next.next.next = newNode(9)
    # head=push(1)
    # head=push(9)
    # head=push(9)
    # head=push(9)
    print("List is: ", end="")
    printList(head)
    head = addOne(head)
    print("\nResultant list is: ", end="")
    printList(head)
