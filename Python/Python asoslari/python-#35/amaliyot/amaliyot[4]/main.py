balans = 100000

try:
    summa = int(input("Qancha pul yechmoqchisiz: "))

    if summa < 0:
        raise ValueError("Manfiy summa kiritib bo'lmaydi!")

    if summa > balans:
        print("Mablag' yetarli emas")
    else:
        balans -= summa
        print(f"Pul yechildi. Qolgan balans: {balans} so'm")

except ValueError as xato:
    print("Xato:", xato)