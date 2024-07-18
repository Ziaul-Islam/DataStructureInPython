def merge(list1, list2):
    combined = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if(list1[i] < list2[j]):
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

#print(merge([4,5,8], [1,2,3,6,7]))

def mergeSort(list):
    if len(list) == 1:
        return list
    midsize = int(len(list) / 2)
    leftlist = mergeSort(list[:midsize])
    rightlist = mergeSort(list[midsize:])

    return merge(leftlist, rightlist)

print(mergeSort([3,2,1,5,4,6,7,9,8]))
