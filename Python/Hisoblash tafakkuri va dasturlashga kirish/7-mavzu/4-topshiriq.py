def selection_sort_visualized(arr):
    n = len(arr)
    print(f"Boshlang'ich massiv: {arr}")
    print("-" * 30)

    for i in range(n):
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        print(f"{i+1}-iteratsiya: {arr}  (Almashtirildi: {arr[i]})")

    print("-" * 30)
    print(f"Saralangan massiv: {arr}")


numbers = [64, 25, 12, 22, 11]
selection_sort_visualized(numbers)