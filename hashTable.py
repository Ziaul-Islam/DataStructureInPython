class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        myhash = 0
        for letter in key:
            myhash = (myhash + ord(letter) * 23) % len(self.data_map)
        return myhash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = [] #create an empty list
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] != None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

myhashtable = HashTable()
myhashtable.set_item('bolts', 1400)
myhashtable.set_item('washers', 50)
myhashtable.set_item('lumber', 70)
print(myhashtable.get_item('bolts'))
print(myhashtable.get_item('washers'))
print(myhashtable.get_item('lumber'))
print(myhashtable.get_item('nails'))
myhashtable.print_table()