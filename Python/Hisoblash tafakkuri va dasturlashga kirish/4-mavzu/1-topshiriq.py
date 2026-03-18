# 1.Qatorning palindrom ekanligini tekshiruvchi is_palindrome (text) funksiyasini 
# yarating (chapdan o‘ngga va o‘ngdan chapga bir xil o‘qiladi). Funksiya True yoki 
# False qiymatini qaytarishi kerak.

def is_palindrome(text):
    text = str(text)
    return text == text[::-1] 

text = input('Biror so\'z kiriting: ')

print(is_palindrome(text))

