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

    def print(self):
        temp = self.first
        print("My Queue : ",end='')
        while temp:
            print(temp.value,", ",end='')
            temp = temp.next
        print("\n")

myQueue = Queue(4)
myQueue.print()