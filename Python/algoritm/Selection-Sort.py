# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         min_idx = i

#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

# def print_array(arr):
#     for val in arr:
#         print(val, end=" ")
#     print()

# if __name__ == "__main__":
#     arr = [64, 25, 12, 22, 11]
    
#     print("Original array: ", end="")
#     print_array(arr)
    
#     selection_sort(arr)
    
#     print("Sorted array: ", end="")
#     print_array(arr)

# -------------------------------------------------------------------------------

# my_array = [64, 34, 25, 5, 22, 11, 90, 12]

# n = len(my_array)
# for i in range(n - 1):
#     min_index = i
#     for j in range(i+1, n):
#         if my_array[j] < my_array[min_index]:
#             min_index = j
#     min_value = my_array.pop(min_index)
#     my_array.insert(i, min_value)

# print("Sorted array:", my_array)

#  ----------------------------------------------------------------------------------

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print("Sorted array:", my_array)