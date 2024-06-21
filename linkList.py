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



myLinkList = LinkList(4)
myLinkList.append(7)
myLinkList.append(23)
myLinkList.append(11)
myLinkList.printList()
print("Pop : ", myLinkList.pop())
print("Pop : ", myLinkList.pop())
print("Pop : ", myLinkList.pop())
print("Pop : ", myLinkList.pop())
print("Pop : ", myLinkList.pop())
myLinkList.printList()
