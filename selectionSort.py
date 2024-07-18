def selection(mylist):
    for i in range(len(mylist)- 1):
        min_ind = i
        for j in range(i+1, len(mylist), 1):
            if mylist[min_ind] > mylist[j]:
                min_ind = j
        if min_ind != i:
            mylist[min_ind], mylist[i] = mylist[i], mylist[min_ind]
    return mylist

mylist = [9, 6, 1, 5, 2, 3]
print(selection(mylist.copy()))
print(mylist)

#Complexity O(n^2)