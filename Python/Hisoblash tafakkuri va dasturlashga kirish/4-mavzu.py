# # 1.Qatorning palindrom ekanligini tekshiruvchi is_palindrome (text) funksiyasini 
# # yarating (chapdan o‘ngga va o‘ngdan chapga bir xil o‘qiladi). Funksiya True yoki 
# # False qiymatini qaytarishi kerak.

# def is_palindrome(text):
#     text = str(text)
#     return text == text[::-1] 

# text = input('Biror so\'z kiriting: ')

# print(is_palindrome(text))



# # 2. n sonning faktorialini hisoblaydigan calculate_factorial (n) funksiyani ishlab 
# # chiqing (n! = 1 × 2 × 3 ×... × n).

# def calculate_factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     return result

# n = int(input('Birorta butun son kiriting: '))

# print(calculate_factorial(n))



# # 3. Ko‘rsatilgan belgidan berilgan o‘lchamdagi to‘g‘ri to‘rtburchakni ekranga 
# # chiqaruvchi draw_rectangle (width, height, symbol) protsedurasini yarating

# def draw_rectangle(width, height, symbol):
#     for i in range(height):
#         print(symbol * width)

# draw_rectangle(5, 3, '#')



# # 4. Satrdagi unli harflar sonini sanaydigan count_vowels (text) funksiyani ishlab 
# # chiqing.

# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
    
#     for char in text:
#         if char in vowels:
#             count += 1
            
#     return count

# print(count_vowels('salom'))



# # 5. Dastlabki n ta Fibonachchi sonlari ro‘yxatini qaytaruvchi generate_fibonacci (n) 
# # funksiyasini yozing.

# def generate_fibonacci(n):
#     fib = []
    
#     a, b = 0, 1
#     for i in range(n):
#         fib.append(a)
#         a, b = b, a + b
        
#     return fib

# print(generate_fibonacci(7))



# # 6.Raqamlar ro'yxatini qabul qiladigan va ularning arifmetik o'rtacha qiymatini 
# # qaytaradigan calculate_average(number_list) funktsiyasini yarating.

# def calculate_average(number_list):
#     total = sum(number_list)
#     count = len(number_list)
#     average = total / count
#     return average

# print(calculate_average([2, 4, 6, 8]))



# # 7. Bir nechta funksiyalar: bosh menyu, ma’lumotlarni kiritish funksiyasi, 
# # ma’lumotlarni qayta ishlash funksiyasi va natijalarni chiqarish funksiyasiga ega 
# # bo‘lgan dastur ishlab chiqish. Dastur turli geometrik shakllar (doira, to‘g‘ri 
# # to‘rtburchak, uchburchak) yuzalarini hisoblashi kerak.

# import math

# def malumot_kiritish(shakl):
#     if shakl == 1:
#         radius = float(input("Doira radiusini kiriting: "))
#         return radius
#     elif shakl == 2:
#         uzunlik = float(input("Uzunlikni kiriting: "))
#         eni = float(input("Enini kiriting: "))
#         return uzunlik, eni
#     elif shakl == 3:
#         asos = float(input("Asosni kiriting: "))
#         balandlik = float(input("Balandlikni kiriting: "))
#         return asos, balandlik


# def yuza_hisoblash(shakl, malumot):
#     if shakl == 1:
#         radius = malumot
#         return math.pi * radius * radius
#     elif shakl == 2:
#         uzunlik, eni = malumot
#         return uzunlik * eni
#     elif shakl == 3:
#         asos, balandlik = malumot
#         return (asos * balandlik) / 2


# def natijani_chiqarish(yuza):
#     print("Hisoblangan yuza:", yuza)


# def bosh_menyu():
#     print("1. Doira yuzi")
#     print("2. To'g'ri to'rtburchak yuzi")
#     print("3. Uchburchak yuzi")

#     tanlov = int(input("Shaklni tanlang (1-3): "))

#     malumot = malumot_kiritish(tanlov)
#     yuza = yuza_hisoblash(tanlov, malumot)
#     natijani_chiqarish(yuza)


# # Dasturni ishga tushirish
# bosh_menyu()