def counting_sort(arr):
    n = len(arr)
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for i in range(n):
        count[arr[i]] += 1
    print(count)
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]
    print(count)
    sorted_arr = [0] * n
    for i in range(n):
        sorted_arr[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    print(count)
    return sorted_arr


arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print(sorted_arr)  
