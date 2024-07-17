class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, current, value):
        if current == None:
            return Node(value)
        if value < current.value:
            current.left = self.__r_insert(current.left, value)
        if value > current.value:
            current.right = self.__r_insert(current.right, value)
        return current
        

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

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
        
    def __r_contains(self, current, srch):
        if current == None:
            return False
        if current.value == srch:
            return True 
        if current.value > srch: #search item is smaller then go left
            return self.__r_contains(current.left, srch)
        elif current.value < srch: #search item is greater then go right 
            return self.__r_contains(current.right, srch)
    
    def r_contains(self, srch):
        return self.__r_contains(self.root, srch)

    
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
    
    def min_value(self, current):
        while current.left is not None:
            current = current.left
        return current.value

    def __delete_node(self, current, value):
        if current == None: #Value to delete is not present
            return None
        if value < current.value: # goto left to delete
             current.left = self.__delete_node(current.left, value)
        elif value > current.value: # goto right to delete
            current.right = self.__delete_node(current.right, value)
        else:
            #Here value to delete. Now we have 4 scenario 
            #1. The leaf node, no right and left
            if current.right == None and current.left == None:
                current = None 
            #2. If only right Node is present
            elif current.left == None:
                current = current.right
            #3. If only left Node is present
            elif current.right == None:
                current = current.left
            #4 If left and right node are present
            else:
                subtree_min = self.min_value(current.right)
                current.value = subtree_min
                current.right = self.__delete_node(current.right, subtree_min)
            return current

    def delete_node(self, value):
        self.__delete_node(self.root, value) 

    def inorderTraversal(self, cur):
        if cur:
            self.inorderTraversal(cur.left)
            print(cur.value,", ", end='')
            self.inorderTraversal(cur.right)

    def preorderTraversal(self, cur):
        if cur:
            print(cur.value,", ", end='')
            self.preorderTraversal(cur.left)
            self.preorderTraversal(cur.right)

    def postorderTraversal(self, cur):
        if cur:
            self.postorderTraversal(cur.left)
            self.postorderTraversal(cur.right)
            print(cur.value,", ", end='')   

myTree = BinarySearchTree()
print(myTree.insert(47))
print(myTree.insert(65))
print(myTree.insert(23))
print(myTree.insert(76))
print(myTree.insert(23))

"""myTree.r_insert(2)
myTree.r_insert(3)
myTree.r_insert(1)"""

print("In-order Traversal: ", end='')
myTree.inorderTraversal(myTree.root)

print("Pre-order Traversal: ", end='')
myTree.preorderTraversal(myTree.root)

print("post-order Traversal: ", end='')
myTree.postorderTraversal(myTree.root)

"""print(myTree.root.value)
print(myTree.root.left.value)
print(myTree.root.right.value)"""

"""print(myTree.root.value)
print(myTree.root.left.value)
print(myTree.root.right.value)
print(myTree.root.right.right.value)"""
"""print("76 : ",myTree.contains(76))
print("23 : ",myTree.contains(23))
print("48 : ",myTree.contains(48))
print("45 : ",myTree.contains(45))
print("97 : ",myTree.contains(97))
print("18 : ",myTree.contains(18))"""
"""print("76 : ",myTree.r_contains(76))
print("23 : ",myTree.r_contains(23))
print("48 : ",myTree.r_contains(48))
print("45 : ",myTree.r_contains(65))
print("97 : ",myTree.r_contains(97))
print("18 : ",myTree.r_contains(65))"""

