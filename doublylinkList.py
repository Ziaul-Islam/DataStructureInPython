class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkList:
    def __init__(self, value):
        new_Node = Node(value)
        self.head = new_Node
        self.tail = new_Node
        self.length = 1
    
    def printList(self):
        temp = self.head
        print("Print the link List:")
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def printList_rev(self):
        temp = self.tail
        print("Print the link List reverse:")
        while temp is not None:
            print(temp.value)
            temp = temp.prev

    def append(self, value):
        new_Node = Node(value)
        if self.head == None and self.tail == None:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            new_Node.prev = self.tail
            self.tail = new_Node
        self.length += 1


        
    
myDoublyLinlList = DoublyLinkList(7)
myDoublyLinlList.append(23)
myDoublyLinlList.append(1)
myDoublyLinlList.append(4)
myDoublyLinlList.printList()
myDoublyLinlList.printList_rev()