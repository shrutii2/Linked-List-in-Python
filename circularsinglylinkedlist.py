# Python code to perform circular linked list operations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.startnode = None

    def insert_at_emptylist(self, data):

        if self.startnode != None:
            return self.startnode
        newNode = Node(data)
        self.startnode = newNode
        self.startnode.next = self.startnode
        return self.startnode

    def insert_at_start(self, data):
        if self.startnode == None:
            return self.insert_at_emptylist(data)
        newNode = Node(data)
        newNode.next = self.startnode.next
        self.startnode.next = newNode
        return self.startnode

    # add node to the end
    def insert_at_end(self, data):
        if self.startnode == None:
            return self.insert_at_emptylist(data)
        newNode = Node(data)
        newNode.next = self.startnode.next
        self.startnode.next = newNode
        self.startnode = newNode
        return self.startnode


    def insert_after_item(self,item,data):
        if self.startnode == None:
            return None
        newNode = Node(data)
        p = self.startnode.next
        while p:
            if p.data == item:
                newNode.next = p.next
                p.next = newNode
                if p == self.startnode:
                    self.startnode = newNode
                    return self.startnode
                else:
                    return self.startnode
            p = p.next
            if p == self.startnode.next:
                print(item, "The given node is not present in the list")
                break

    def traverse(self):
        if self.startnode == None:
            print("The list is empty")
            return
        newNode = self.startnode.next
        while newNode:
            print(newNode.data, end=" ")
            newNode = newNode.next
            if newNode == self.startnode.next:
                break

    def deleteNode(self,head, key) :
        if (head == None):
            return
        if((head).data == key and (head).next == head):
            head = None
        last = head
        d = None
        if((head).data == key) :
            while(last.next != head):
                last = last.next
            last.next = (head).next
            head = last.next
        while(last.next != head and last.next.data != key) :
            last = last.next
        if(last.next.data == key) :
            d = last.next
            last.next = d.next
        else:
            print("no such keyfound")
        return head


cll = CircularLinkedList()
head=None
head=cll.insert_at_emptylist(2)
head=cll.insert_at_end(10)
head=cll.insert_after_item(2,5)
# cll.insert_at_start(2)
head=cll.insert_after_item(5,7)
head=cll.insert_after_item(7,8)
print('before deletion: ',end='')
cll.traverse()
head=cll.deleteNode(head,7)
print('\nafter deletion: ',end='')
cll.traverse()
