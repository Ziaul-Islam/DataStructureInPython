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
            print(temp.value," ,", end=" ")
            temp = temp.next
        print()
    
    def printList_rev(self):
        temp = self.tail
        print("Print the link List reverse:")
        while temp is not None:
            print(temp.value," ,", end=" ")
            temp = temp.prev
        print()

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
        return True
    
    def pop(self):
        temp = None
        if self.head == None and self.tail == None:
            return None
        elif self.head == self.tail:
            temp = self.head
            self.head = self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value
    
    def get(self, index):
        if index >= self.length or index < 0:
            return None
        temp = self.head 
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is None:
            return False
        else:
            temp.value = value
            return True
        

    
myDoublyLinlList = DoublyLinkList(7)
myDoublyLinlList.append(23)
myDoublyLinlList.append(1)
myDoublyLinlList.append(4)
myDoublyLinlList.printList()
#myDoublyLinlList.printList_rev()
#print("My pop item is ",myDoublyLinlList.pop())
#myDoublyLinlList.printList()
"""
print("Index 3 : ",myDoublyLinlList.get(3))
print("Index 5 : ",myDoublyLinlList.get(5))
print("Index -1 : ",myDoublyLinlList.get(-1))
"""
myDoublyLinlList.set_value(3, 90)
myDoublyLinlList.printList()
