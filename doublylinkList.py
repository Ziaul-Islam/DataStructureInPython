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
    
myDoublyLinlList = DoublyLinkList(7)
myDoublyLinlList.printList()