import json

# yosh = input("Yoshingizni kiriting:  ")
# yosh = int(yosh)
# print(f"Siz {2026-yosh}-yilda tug'ilgansiz.")

# yosh = input("Yoshingizni kiriting:  ")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2026-yosh}-yilda tug'ilgansiz")
    
# print("Dastur tugadi!")

# x, y = 5, 10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")

# mevalar = ["olma", "anor", "anjir", "uzum"]

# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xalos.")

# user ={
#     'username':"sariqdev",
#     'status': "admin",
#     'email': "admin@sariq.dev",
#     'phone': 99897123456 
# }

# key = 'tel'

# try:
#     print(f"Foydalanuvchi {user[key]}")

# except KeyError:
#     print("Bunday kalit mavjud emas!")

# filename = 'data.txt'
# try:
#     with open(filename) as file:
#         text = file.read()
    
# except FileNotFoundError:
#     print(f"{filename} mavjud emas. Boshqa fayl tanlang")

# n = input("Butun son kiriting: ")

# try:
#     n = int(n)
#     x = 20/n
# except ValueError:
#     print("Butun son kiritmadingiz!")
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas!")
# else:
#     print(f"x = {x}")

# talaba1 = {
#     'ism':'Alijon Valiyev',
#     'kurs': 2
# }
# talaba2 = {
#     'ism':'Hasan Husanov',
#     'kurs':1
# }

# talaba4 = {
#     'ism': 'Olim Olimov',
#     'kurs':3
# }
# with open('talaba1.json', 'w') as file:
#     json.dump(talaba1, file)
# with open('talaba2.json', 'w') as file:
#     json.dump(talaba2, file)
# with open('talaba4.json', 'w') as file:
#     json.dump(talaba4, file)


# files = ['talaba1.json', 'talaba2.json','talaba3.json', 'talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as file:
#             talaba =  json.load(file)
#     except FileNotFoundError:
#         # print(f"{filename} mavjud emas")
#         pass
#     else:
#         print(talaba['ism'])

while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break

print(f"Siz {2026-yosh}- yilda tug'ilgansiz.")
