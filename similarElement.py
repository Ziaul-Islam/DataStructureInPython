def similar(list1, list2):
    dict = {}
    for i in list1:
        dict[i] = True
    for j in list2:
        if j in dict:
            return True
    return False

list1 = [2,3,5]
list2 = [4,7,6]

print(similar(list1, list2))
