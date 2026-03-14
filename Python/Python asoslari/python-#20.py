# def toliq_ism_yasa(ism, familiya):
#     """To\'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f'{ism.title()} {familiya.title()}'
#     return toliq_ism

# talaba1 = toliq_ism_yasa('olim', 'hakimov')
# talaba2 = toliq_ism_yasa('hakim', 'olimov')

# print(f'Darsga kelmagan talabalar: {talaba1} va {talaba2}')

# def toliq_ism_yasa(ism, familiya, otasining_ismi = ''):
#     """To\'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f'{ism.title()} {otasining_ismi.title()} {familiya.title()}'
#     else:
#         toliq_ism = f'{ism.title()} {familiya.title()}'
    
#     return toliq_ism

# talaba1 = toliq_ism_yasa('olim', 'hakimov')
# talaba2 = toliq_ism_yasa('hakim', 'olimov', 'abrorovich')
# print(f'Darsga kelmagan talbalar: {talaba1} va {talaba2}')

# def avto_info(kompaniya, model, rangi, karobka, yili, narhi = None):
#     avto = {
#         'kompaniya':kompaniya,
#         'model':model,
#         'rang':rangi,
#         'karobka':karobka,
#         'yil': yili, 
#         'narh':narhi
#     }
#     return avto

# avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
# avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016, 15000)

# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')

# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = 'Noma\'lum'
#     print(f'{avto['rang']} {avto['model']}, Narhi: {narh}')

# def oraliq(min, max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar

# print(oraliq(0, 10))
# print(oraliq(10, 20))

# def oraliq(min, max, qadam = 1):
#     sonlar = []
#     while min < max :
#         sonlar.append(min)
#         min += qadam
#     return sonlar

# print(oraliq(0, 21, 2))

# print('Saytimizdagi avtolar ro\'yhatini shakllantiramiz')

# avtolar = []
# while True:
#     print('\nQuyudagi ma\'alumotlarni kiriting:', end = '')
#     kompaniya = input('Ishlab chiqaruvchi: ')
#     model = input('Model: ')
#     rang = input('Rangi: ')
#     karobka = input('Karobka: ')
#     yil = input('Ishlab chiqarilgan yili: ')
#     narh = input('Narhi: ')

#     avtolar.append(avto_info(kompaniya, model, rang, karobka, yil, narh))

#     javob = input('Yana avto qo\'shasizmi?  (yes/no): ')
    
#     if javob == 'no':
#         break


# for avto in avtolar:
#     print(f'{avto['rang'].title()} {avto['model'].title()}, {avto['karobka'].title()} karobka. Narhi: {avto['narh']}')


# from datetime import datetime

# def foydalanuvchi_malumotlari(ism, familiya, tugilgan_yil, tugilgan_joy, email=None, telefon=None):
#     hozirgi_yil = datetime.now().year
#     yosh = hozirgi_yil - tugilgan_yil

#     foydalanuvchi = {
#         "ism": ism,
#         "familiya": familiya,
#         "tugilgan_yil": tugilgan_yil,
#         "tugilgan_joy": tugilgan_joy,
#         "yosh": yosh
#     }

#     if email:
#         foydalanuvchi["email"] = email
#     if telefon:
#         foydalanuvchi["telefon"] = telefon

#     return foydalanuvchi


# # Misol uchun chaqirish
# malumot = foydalanuvchi_malumotlari(
#     "Ali",
#     "Karimov",
#     2003,
#     "Toshkent",
#     email="ali@gmail.com",
#     telefon="+998901234567"
# )

# print(malumot)

# mijozlar = []

# while True:
#     print("\nYangi foydalanuvchi ma'lumotlarini kiriting")

#     ism = input("Ism: ")
#     familiya = input("Familiya: ")
#     tugilgan_yil = int(input("Tug'ilgan yil: "))
#     tugilgan_joy = input("Tug'ilgan joy: ")
#     email = input("Email (ixtiyoriy): ")
#     telefon = input("Telefon raqam (ixtiyoriy): ")

#     foydalanuvchi = foydalanuvchi_malumotlari(
#         ism, familiya, tugilgan_yil, tugilgan_joy, email, telefon
#     )

#     mijozlar.append(foydalanuvchi)

#     yana = input("Yana foydalanuvchi qo'shasizmi? (ha/yo'q): ")
#     if yana.lower() != "ha":
#         break


# print("\nMijozlar ro'yxati:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism']} {mijoz['familiya']}, "
#           f"Yosh: {mijoz['yosh']}, "
#           f"Tug'ilgan joyi: {mijoz['tugilgan_joy']}, "
#           f"Email: {mijoz['email']}, "
#           f"Telefon: {mijoz['telefon']}")

# def eng_katta(a, b, c):
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c
    
# a = []

# for i in range(3):
#     x = input(f'{i+1}-sonni kiriting: ')
#     a.append(int(x))

# print(eng_katta(a[0], a[1], a[2])) 

# def shakl_malumotlari(radius):
#     diametr = 2 * radius
#     perimetr = diametr * 3.14
#     yuza = 3.14 * radius * radius
#     return {
#         'radius': radius,
#         'diametr': diametr,
#         'perimetr': perimetr,
#         'yuza': yuza
#     }

# radius = input('Aylana radiusini kiriting: ')

# print(shakl_malumotlari(float(radius)))

# import math
# def tub_sonlar(a, b):
#     """Berilgan oraliqdagi tub sonlar ro\'yhati"""
#     tub = []
#     for i in range(a, b+1):
#         isTub = True
#         if i==1:
#             isTub = False
#         for j in range(2, int(math.sqrt(i))+1):
#             if i%j==0:
#                 isTub =False
#                 break
#         if isTub:
#             tub.append(i)
#     return tub

# print(len(tub_sonlar(1, 1000)))
        
# def fibonachi_sonlar(n):
#     fib = []
#     a = 0
#     b = 1
#     for i in range(n):
#         fib.append(a)
#         a, b = b, a+b
#     return fib
# print(fibonachi_sonlar(50))
