arr=[2,4,1,6,5,12,3,36,7,8]

m=len(arr)//2    #O(nlogn)
def MergeSort(arr):
    if len(arr)==1:
        return arr
    la=MergeSort(arr[:len(arr)//2])
    ra=MergeSort(arr[len(arr)//2:])
    i, j, k = 0, 0, 0
    #print(la, ra, arr, sep=" // ")
    while (i < len(la) and j < len(ra)):
        if la[i] <= ra[j]:
            arr[k] = la[i]
            k += 1
            i += 1
        else:
            arr[k] = ra[j]
            k += 1
            j += 1
    while (i < len(la)):
        arr[k] = la[i]
        k += 1
        i += 1
    while (j < len(ra)):
        arr[k] = ra[j]
        k += 1
        j += 1
    return arr


print(MergeSort(arr))
