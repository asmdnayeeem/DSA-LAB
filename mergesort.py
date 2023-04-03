def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        M = arr[mid:]
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1
    return arr

data = map(int, input("Enter the list of numberes:").split(","))
data = list(data)
print('Sorted list in Ascending Order:')
arr=mergeSort(data)
print("Sorted list is: ")
print(arr)