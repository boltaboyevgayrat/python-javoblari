def binary_search_sqrt(n, precision):
    if n < 0:
        return "Manfiy sonning haqiqiy kvadrat ildizi mavjud emas"
    
    # 1 dan kichik sonlar uchun yuqori chegara 1 bo'lishi kerak
    low = 0
    high = max(1, n)
    
    # Berilgan aniqlik darajasiga (masalan 0.00001) yetguncha davom etamiz
    while (high - low) > precision:
        mid = (low + high) / 2
        
        if mid * mid < n:
            low = mid
        else:
            high = mid
            
    return (low + high) / 2

# Sinov
number = 2
epsilon = 0.00001
result = binary_search_sqrt(number, epsilon)

print(f"{number} ning kvadrat ildizi taxminan: {result:.5f}")
print(f"Tekshirish: {result} * {result} = {result * result}")