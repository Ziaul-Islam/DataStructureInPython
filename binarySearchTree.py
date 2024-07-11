class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_Node = Node(value)
        if self.root == None:
            self.root = new_Node
            return True
        else:
            temp = self.root
            while temp is not None:
                if temp.value == new_Node.value:
                    return False # No duplicate
                elif new_Node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_Node
                        return True
                    temp = temp.left
                elif new_Node.value > temp.value:
                    if temp.right is None:
                        temp.right = new_Node
                        return True
                    temp = temp.right
    
    def contains(self, srch):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if temp.value == srch:
                return True
            elif srch < temp.value:
                temp = temp.left
            elif srch > temp.value:
                temp = temp.right
        return False



myTree = BinarySearchTree()
print(myTree.insert(47))
print(myTree.insert(65))
print(myTree.insert(23))
print(myTree.insert(76))
print(myTree.insert(23))
"""print(myTree.root.value)
print(myTree.root.left.value)
print(myTree.root.right.value)
print(myTree.root.right.right.value)"""
print("76 : ",myTree.contains(76))
print("23 : ",myTree.contains(23))
print("48 : ",myTree.contains(48))
print("45 : ",myTree.contains(45))
print("97 : ",myTree.contains(97))
print("18 : ",myTree.contains(18))
