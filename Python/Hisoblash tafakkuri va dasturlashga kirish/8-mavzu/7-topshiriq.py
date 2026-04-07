def find_min_platforms(arrival, departure):
    # 1. Kelish va jo'nash vaqtlarini mustaqil ravishda saralaymiz
    arrival.sort()
    departure.sort()

    n = len(arrival)
    platforms_needed = 0
    max_platforms = 0
    
    i = 0  # Kelish vaqtlari uchun ko'rsatkich
    j = 0  # Jo'nash vaqtlari uchun ko'rsatkich

    # Barcha poyezdlarni ko'rib chiqamiz
    while i < n and j < n:
        # Agar keyingi voqea - poyezd kelishi bo'lsa
        if arrival[i] <= departure[j]:
            platforms_needed += 1
            i += 1
        # Agar keyingi voqea - poyezd jo'nashi bo'lsa
        else:
            platforms_needed -= 1
            j += 1
        
        # Maksimal kerak bo'lgan platformalar sonini yangilaymiz
        max_platforms = max(max_platforms, platforms_needed)

    return max_platforms

# Sinov ma'lumotlari (vaqtlar soniya yoki minut formatida bo'lishi mumkin)
# Masalan: 9:00, 9:40, 9:50, 11:00, 15:00, 18:00
arr = [900, 940, 950, 1100, 1500, 1800]
# Masalan: 9:10, 12:00, 11:20, 11:30, 19:00, 20:00
dep = [910, 1200, 1120, 1130, 1900, 2000]

result = find_min_platforms(arr, dep)
print(f"Zarur bo'lgan minimal platformalar soni: {result}")