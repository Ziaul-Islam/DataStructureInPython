class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return (index * 2) + 1 # Adding 1 because the index starts with 0
    
    def _right_child(self, index):
        return (index * 2) + 2 # 1 for index + 1 for right child
    
    def _parent_index(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1] 

    def _sink_down(self, index): #to sink the first element down to correct place
        max_index = index
        while True:
            left_child = self._left_child(index)
            right_child = self._right_child(index)

            if left_child < len(self.heap) and self.heap[max_index] < self.heap[left_child]:
                max_index = left_child
            if right_child < len(self.heap) and self.heap[max_index] < self.heap[right_child]:
                max_index = right_child
            if max_index != index:
                self._swap(max_index,index)
                index = max_index
            else: #break the heap is balance 
                return   

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1 # pos of currently added value
        while current > 0 and self.heap[current] > self.heap[self._parent_index(current)]:
            self._swap(current, self._parent_index(current)) #at this step current > parent
            current = self._parent_index(current) #jump to parent

    def remove(self):
        # only remove the first/highest element from list
        if len(self.heap) == 0: #cond 1. no item
            return None
        elif len(self.heap) == 1: #cond 2. 1 item
            return self.heap.pop()
        else: #cond 3. more than 1 item
            max_value = self.heap[0]
            self.heap[0] = self.heap.pop() #update the first item with the last
            self._sink_down(0) # put the first value in current place
            return max_value


    
    def print_heap(self):
        print("My Max Heap")
        for i, val in enumerate(self.heap):
            print(i," : ", val)

myheap = MaxHeap()
myheap.insert(72)
myheap.insert(75)
myheap.insert(66)
myheap.insert(61)
myheap.insert(58)
myheap.insert(100)
myheap.print_heap()
myheap.insert(99)
myheap.print_heap()
print("Remove : ",myheap.remove())
myheap.print_heap()
