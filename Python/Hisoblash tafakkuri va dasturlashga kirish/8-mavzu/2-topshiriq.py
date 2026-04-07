def count_in_range(arr, num, low, high):
    """Berilgan oraliqda son necha marta qatnashganini sanaydi"""
    count = 0
    for i in range(low, high + 1):
        if arr[i] == num:
            count += 1
    return count

def get_majority_element(arr, low, high):
    # Bazaviy holat: massivda bitta element qolsa
    if low == high:
        return arr[low]

    # Massivni o'rtasidan bo'lamiz
    mid = (low + high) // 2
    
    # Chap va o'ng yarimlar uchun g'olibni topamiz
    left_winner = get_majority_element(arr, low, mid)
    right_winner = get_majority_element(arr, mid + 1, high)

    # Agar ikkala yarimda ham bir xil element g'olib bo'lsa
    if left_winner == right_winner:
        return left_winner

    # Agar g'oliblar turlicha bo'lsa, ularni butun oraliqda sanaymiz
    left_count = count_in_range(arr, left_winner, low, high)
    right_count = count_in_range(arr, right_winner, low, high)

    return left_winner if left_count > right_count else right_winner

# Sinov
data = [2, 2, 1, 1, 1, 2, 2]
n = len(data)
result = get_majority_element(data, 0, n - 1)

# n/2 dan ko'p uchrashini tekshirish
if data.count(result) > n // 2:
    print(f"Ko'pchilik element: {result}")
else:
    print("Ko'pchilik element mavjud emas")
