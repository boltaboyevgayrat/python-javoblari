def binary_search(arr, item):
    low = 0
    high = len(arr)-1
    while high >= low:
        mid = int((high + low)/2)
        if arr[mid] == item:
            return mid
        if arr[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

print(binary_search(arr, 19))