def bubble(mylist):
    for i in range(len(mylist) - 1, 0, -1):
        for j in range(i): #remeber last value of range is exclusive
            if mylist[j] > mylist[j+1]:
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp
    return mylist


mylist = [9, 6, 1, 5, 2, 3]
print(bubble(mylist.copy()))
print(mylist)