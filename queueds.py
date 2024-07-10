class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#In queue add at last and delete from first
class Queue:
    def __init__(self, value):
        new_Node = Node(value)
        self.first = new_Node
        self.last = new_Node
        self.length = 1

    def print(self):
        temp = self.first
        print("My Queue : ",end='')
        while temp:
            print(temp.value,", ",end='')
            temp = temp.next
        print("\n")

    def enqueue(self, value):
        new_Node = Node(value)
        if self.length == 0:
            self.first = new_Node
            self.last = new_Node
            self.length = 1
        else:
            self.last.next = new_Node
            self.last = new_Node
            self.length += 1
    
    def dequeue(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.first
            self.first = None
            self.last = None
            self.length = 0
            return temp.value
        else:
            temp = self.first
            self.first = self.first.next
            self.length -= 1
            return temp.value
        
myQueue = Queue(4)
myQueue.enqueue(11)
myQueue.enqueue(7)
myQueue.enqueue(23)
myQueue.print()
print(myQueue.dequeue())
myQueue.print()
print(myQueue.dequeue())
myQueue.print()
print(myQueue.dequeue())
myQueue.print()
print(myQueue.dequeue())
myQueue.print()
print(myQueue.dequeue())
myQueue.print()
myQueue.enqueue(87)
myQueue.enqueue(3)
myQueue.print()