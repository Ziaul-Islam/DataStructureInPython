def insertion(mylist):
    for i in range(1, len(mylist)):
        temp = mylist[i]
        j = i - 1
        while temp < mylist[j] and j > -1:
            mylist[j+1] = mylist[j]
            mylist[j] = temp
            j -= 1
    return mylist

mylist = [9, 6, 1, 5, 2, 3]
print(insertion(mylist.copy()))
print(mylist)
