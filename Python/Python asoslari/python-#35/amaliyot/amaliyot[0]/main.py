# try:
#     son = int(input("Sonni kiriting: "))
#     natija = 10/son
#     print(f"Natija: {natija}")
# except ZeroDivisionError:
#     print('Xato. Sonni no\'lga bo\'lish mumkin emas!')

# except ValueError:
#     print('Xato. Faqat butun son kiriting!')

# yosh = -5
# if yosh < 0:
#     raise Exception("Yosh manfiy bo'lishi mumkin emas!")

class MyCustomError(Exception):
    pass

raise MyCustomError('Mening shaxsiy xatoligim!')