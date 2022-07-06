

class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def insert_in_emptylist(self,data):
        if self.head is None:
            newnode=Node(data)
            self.head=newnode
        else:
            print("List is not empty")

    def insert_at_start(self,data):
        if self.head is None:
            newnode=Node(data)
            self.head=newnode
            print("Node inserted")
            return
        newnode=Node(data)
        newnode.nref=self.head
        self.head.pref=newnode
        self.head=newnode

    def insert_at_end(self,data):
        if self.head is None:
            newnode=Node(data)
            self.head=newnode
            return
        n=self.head
        while n.nref is not None:
            n=n.nref
        newnode=Node(data)
        n.nref=newnode
        newnode.pref=n

    def insert_after_data(self,x,data):
        if self.head is None:
            print("List is empty")
            return
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            if n is None:
                print("data not in list")
            else:
                newnode=Node(data)
                newnode.pref=n
                newnode.nref=n.nref
                if n.nref is not None:
                    n.nref.prev=newnode
                n.nref=newnode

    def insert_before_data(self,x,data):
        if self.head is None:
            print("LIst is empty")
            return
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            if n is None:
                print("data not in list")
            else:
                newnode=Node(data)
                newnode.nref=n
                newnode.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=newnode
                n.pref=newnode

    def traverse_list(self):
        if self.head is None:
            print("List has no data")
            return
        else:
            n=self.head
            while n is not None:
                print(n.data,' ')
                n=n.nref

    def delete_at_start(self):
        if self.head is None:
            print("List has no element to delete")
            return
        if self.head.nref is None:
            self.head=None
            return
        self.head=self.head.nref
        self.startprev=None

    def delete_at_end(self):
        if self.head is None:
            print("List has no element to delete")
            return
        if self.head.nref is None:
            self.head=None
            return
        n=self.head
        while n.nref is not None:
            n=n.nref
        n.pref.nref=None

    def delete_element_by_value(self,x):
        if self.head is None:
            print("List has no element to delete")
            return
        if self.head.nref is None:
            if self.head.data==x:
                self.head=None
            else:
                print("data not found")
            return
        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
            return
        n=self.head
        while n.nref is not None:
            if n.data==x:
                break
            n=n.nref
        if n.nref is not None:
            n.pref.nref=n.nref
            n.nref.pref=n.pref
        else:
            if n.data==x:
                n.pref.nref=None
            else:
                print("ELement not found")

    def reverse(self):
        if self.head is None:
            print("List has no elememt to delete")
            return
        p=self.head
        q=p.nref
        p.nref=None
        p.pref=q
        while q is not None:
            q.pref=q.nref
            q.nref=p
            p=q
            q=q.pref
        self.head=p

def reverse(llist):
    # Write your code here
    if llist == None or llist.next == None:
        return llist
    
    while True:
        temp = llist.next
        llist.next = llist.prev
        llist.prev = temp
        llist = llist.prev
        
        if llist.next == None:
            break
    temp = llist.next
    llist.next = llist.prev
    llist.prev = temp
    return llist


D=DoublyLinkedList()
D.insert_in_emptylist(50)
D.insert_at_start(10)
D.insert_at_start(5)
D.insert_at_start(18)
D.insert_at_end(29)
D.insert_at_end(39)
D.insert_after_data(5,9)
D.insert_before_data(29,19)
D.traverse_list()
print(" ")
# D.delete_at_start()
# D.delete_at_end()
# D.delete_element_by_value(54)
# D.traverse_list()
# print(" ")
D.reverse()
D.traverse_list()