def swap(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]

def pivot(list, pivot_idx, end_idx) -> int:
    swap_idx = pivot_idx
    for i in range(pivot_idx + 1, end_idx + 1):
        if list[pivot_idx] > list[i]:
            swap_idx += 1
            swap(list, swap_idx, i)
    swap(list, pivot_idx, swap_idx)
    return swap_idx

def quickSort(list):
    def quick(list, left, right):
        if left < right:  
            pivot_idx = pivot(list, left, right)
            quick(list, left, pivot_idx - 1)
            quick(list, pivot_idx + 1, right)
        return list
    return quick(list, 0, len(list) - 1)
       
list = [4,6,1,7,3,2,5]
print(list)
print("Quick Sorted list : ")
print(quickSort(list))
