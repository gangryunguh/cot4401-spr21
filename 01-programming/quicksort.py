
def quicksort(arr):

    def partition(first, last):
        # use "last" as the pivot index
        pivot_val = arr[last]
        i = first-1
        for j in range(first,last):
            if arr[j] < pivot_val:
                i += 1
                arr[i],arr[j] = arr[j],arr[i]

        arr[i+1],arr[last] = arr[last],arr[i+1]
        return i+1


    def qsort(first, last):
        if first < last:
            pivot = partition(first, last)
            qsort(first,pivot-1)
            qsort(pivot+1,last)

    qsort(0,len(arr)-1)


arr = [2, 5, 1, 9, 4, 10, 15, 12, -4, -3, 20, 28, 7, 8]
print("Before sorting:")
print(arr)
quicksort(arr)
print("After sorting:")
print(arr)
