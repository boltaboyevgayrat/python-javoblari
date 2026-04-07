def count_inversions(arr):
    # Asosiy rekursiv funksiya
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left_half, left_inv = count_inversions(arr[:mid])
    right_half, right_inv = count_inversions(arr[mid:])
    
    merged, split_inv = merge_and_count(left_half, right_half)
    
    return merged, left_inv + right_inv + split_inv

def merge_and_count(left, right):
    result = []
    i = j = 0
    count = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            # Inversiya topildi!
            # left[i] dan keyingi barcha elementlar ham right[j] dan katta
            result.append(right[j])
            count += (len(left) - i)
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result, count

# Sinov
data = [8, 4, 2, 1]
sorted_arr, total_inversions = count_inversions(data)

print(f"Massiv: {data}")
print(f"Inversiyalar soni: {total_inversions}")
# Tushuntirish: (8,4), (8,2), (8,1), (4,2), (4,1), (2,1) -> Jami 6 ta