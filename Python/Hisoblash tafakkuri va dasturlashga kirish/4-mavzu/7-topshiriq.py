# 7. Bir nechta funksiyalar: bosh menyu, ma’lumotlarni kiritish funksiyasi, 
# ma’lumotlarni qayta ishlash funksiyasi va natijalarni chiqarish funksiyasiga ega 
# bo‘lgan dastur ishlab chiqish. Dastur turli geometrik shakllar (doira, to‘g‘ri 
# to‘rtburchak, uchburchak) yuzalarini hisoblashi kerak.

import math

def malumot_kiritish(shakl):
    if shakl == 1:
        radius = float(input("Doira radiusini kiriting: "))
        return radius
    elif shakl == 2:
        uzunlik = float(input("Uzunlikni kiriting: "))
        eni = float(input("Enini kiriting: "))
        return uzunlik, eni
    elif shakl == 3:
        asos = float(input("Asosni kiriting: "))
        balandlik = float(input("Balandlikni kiriting: "))
        return asos, balandlik


def yuza_hisoblash(shakl, malumot):
    if shakl == 1:
        radius = malumot
        return math.pi * radius * radius
    elif shakl == 2:
        uzunlik, eni = malumot
        return uzunlik * eni
    elif shakl == 3:
        asos, balandlik = malumot
        return (asos * balandlik) / 2


def natijani_chiqarish(yuza):
    print("Hisoblangan yuza:", yuza)


def bosh_menyu():
    print("1. Doira yuzi")
    print("2. To'g'ri to'rtburchak yuzi")
    print("3. Uchburchak yuzi")

    tanlov = int(input("Shaklni tanlang (1-3): "))

    malumot = malumot_kiritish(tanlov)
    yuza = yuza_hisoblash(tanlov, malumot)
    natijani_chiqarish(yuza)


# Dasturni ishga tushirish
bosh_menyu()