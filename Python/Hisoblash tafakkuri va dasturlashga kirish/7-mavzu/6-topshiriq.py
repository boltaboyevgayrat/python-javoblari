import random
import time

def quick_sort(arr, pivot_type="last"):
    if len(arr) <= 1:
        return arr
    
    if pivot_type == "first":
        pivot = arr[0]
        rest = arr[1:]
    elif pivot_type == "last":
        pivot = arr[-1]
        rest = arr[:-1]
    elif pivot_type == "middle":
        mid = len(arr) // 2
        pivot = arr[mid]
        rest = arr[:mid] + arr[mid+1:]
    elif pivot_type == "random":
        rand_idx = random.randint(0, len(arr) - 1)
        pivot = arr[rand_idx]
        rest = arr[:rand_idx] + arr[rand_idx+1:]

    left = [x for x in rest if x <= pivot]
    right = [x for x in rest if x > pivot]
    
    return quick_sort(left, pivot_type) + [pivot] + quick_sort(right, pivot_type)

test_data = list(range(2000))

start = time.time()
try:
    quick_sort(test_data, "first")
except RecursionError:
    print("First pivot: Rekursiya limiti oshib ketdi!")
print(f"First pivot vaqti: {time.time() - start:.5f} sek")

start = time.time()
quick_sort(test_data, "random")
print(f"Random pivot vaqti: {time.time() - start:.5f} sek")