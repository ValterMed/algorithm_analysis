def maxsub(arr):
    maxend = maxsof = arr[0]
    for i in arr[1:]:
        maxend = max(i, maxend + i)
        maxsof = max(maxsof, maxend)
    return maxsof

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Maximum subarray sum: {maxsub(arr)}")