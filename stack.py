class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
#In stact we add and delete from top
class Stack:
    def __init__(self, value):
        new_Node = Node(value)
        self.top = new_Node
        self.height = 1
    
    def printStack(self):
        temp = self.top
        print("My Stack : ")
        while temp != None:
            print(temp.value,", ",end='')
            temp = temp.next
        print("\n")
    
    def push(self, value):
        new_Node = Node(value)
        new_Node.next = self.top
        self.top = new_Node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp.value

myStack = Stack(11)
myStack.push(7)
myStack.push(3)
myStack.printStack()
print("My Stack Top : ", myStack.top.value)
print("My Stack pop: ", myStack.pop())
print("My Stack pop: ", myStack.pop())
print("My Stack pop: ", myStack.pop())
print("My Stack pop: ", myStack.pop())
        
        