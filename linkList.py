#Node 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkList:
    def __init__(self, value):
        newNode = Node(value) #newNode is not self why.
        self.head = newNode
        self.tail = newNode
        self.length = 1
    
    def printList(self):
        print("Print the link List:")
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return -1
        elif self.head == self.tail:
            temp = self.head
            self.head = self.tail = None
        else:
            pre = self.head
            temp = pre.next
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        return temp.value
    
    def set_value(self, index, value):
        if index < 0 or self.length == -1:
            return False
        else:
            temp = self.head
            i = 0
            while temp != None and i < index:
                temp = temp.next
                i += 1
            if temp is None: 
                return False
            else:
                temp.value = value
                return True
    
    def reverse_linklist(self):
        pre = self.head
        self.head = self.tail
        self.tail = pre
        cur = None
        if pre != None:
            cur = pre.next
            pre.next = None
        while cur is not None:
            temp = cur.next 
            cur.next = pre 
            pre = cur 
            cur = temp





myLinkList = LinkList(4)
myLinkList.append(7)
myLinkList.append(23)
myLinkList.append(11)
myLinkList.printList()
#print("Pop : ", myLinkList.pop())
"""
print("Pop : ", myLinkList.pop())
print("Pop : ", myLinkList.pop())
print("Pop : ", myLinkList.pop())
print("Pop : ", myLinkList.pop())
"""
#myLinkList.printList()
"""
print(myLinkList.set_value(0, 1))
print(myLinkList.set_value(1, 2))
print(myLinkList.set_value(2, 3))
print(myLinkList.set_value(3, 4))
print(myLinkList.set_value(-1, 404))
myLinkList.printList()
"""
myLinkList.reverse_linklist();
myLinkList.printList()
