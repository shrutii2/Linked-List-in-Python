# T(n)=O(n) S(n)=O(n) if function call stack size is considered,otherwise O(1)
# recursive method
head = None
left = None
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def isPalindromeUtil(right):
    global head, left
    left = head
    if (right == None):
        return True
    isp = isPalindromeUtil(right.next)
    if (isp == False):
        return False
    isp1 = (right.data == left.data)
    left = left.next
    return isp1

def isPalindrome(head):
    result = isPalindromeUtil(head)
    return result

def push(new_data):
    global head
    new_node = Node(new_data)
    new_node.next = head
    head = new_node

def printList(ptr):
    while (ptr != None):
        print(ptr.data, end="->")
        ptr = ptr.next
    print("Null ")

# Driver Code
str = ['a', 'b', 'a', 'c', 'a', 'b', 'a']
  
for i in range(0, 7):
    push(str[i])
    printList(head)

    if (isPalindrome(head) and i != 0):
        print("Is Palindrome\n")
    else:
        print("Not Palindrome\n")

# by reversing : T(n)=O(n) S(n)=O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isPalindrome(self, head):
        slow_ptr = head
        fast_ptr = head
        prev_of_slow_ptr = head
        midnode = None
        res = True  
        
        if (head != None and head.next != None):
            while (fast_ptr != None and fast_ptr.next != None):
                fast_ptr = fast_ptr.next.next
                prev_of_slow_ptr = slow_ptr
                slow_ptr = slow_ptr.next
            if (fast_ptr != None):
                midnode = slow_ptr
                slow_ptr = slow_ptr.next
            second_half = slow_ptr
            prev_of_slow_ptr.next = None 
            second_half = self.reverse(second_half) 
            res = self.compareLists(head, second_half)  
            second_half = self.reverse(second_half)
            if (midnode != None):
                prev_of_slow_ptr.next = midnode
                midnode.next = second_half
            else:
                prev_of_slow_ptr.next = second_half
        return res

    def reverse(self, second_half):
        prev = None
        current = second_half
        next = None
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        second_half = prev
        return second_half

    def compareLists(self, head1, head2):
        temp1 = head1
        temp2 = head2
        while (temp1 and temp2):
            if (temp1.data == temp2.data):
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return 0
        if (temp1 == None and temp2 == None):
            return 1
        return 0

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = "->")
            temp = temp.next
        print("NULL")

# Driver code
if __name__ == '__main__':
    l = LinkedList()
    s = [ 'a', 'b', 'a', 'c', 'a', 'b', 'a' ]
    for i in range(7):
        l.push(s[i])
        l.printList()
        if (l.isPalindrome(l.head) != False):
            print("Is Palindrome\n")
        else:
            print("Not Palindrome\n")
        print()