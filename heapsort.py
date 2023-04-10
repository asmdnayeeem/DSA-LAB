def heapify(arr, n, i):
    largest = i  # initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # if left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # if right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # if largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # recursively heapify the affected sub-tree
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    return arr


arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print(sorted_arr)  # Output: [5, 6, 7, 11, 12, 13]
