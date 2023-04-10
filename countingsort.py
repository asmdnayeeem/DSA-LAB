def counting_sort(arr):
    n = len(arr)
    max_val = max(arr)  # find the maximum value in the array
    count = [0] * (max_val + 1)  # initialize the count array
    print(count)
    # count the frequency of each element in the array
    for i in range(n):
        count[arr[i]] += 1

    # modify the count array to store the actual position of each element in the sorted array
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    # create the sorted array
    sorted_arr = [0] * n
    for i in range(n):
        sorted_arr[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return sorted_arr


arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print(sorted_arr)  # Output: [1, 2, 2, 3, 3, 4, 8]
