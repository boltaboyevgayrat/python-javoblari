# car0 = {
#     'model':'lacetti',
#     'rang':'oq',
#     'yil':2018,
#     'narh':13000,
#     'km':50000,
#     'korobka':'avtomat'
# }
# car1 = {
#     'model':'nexia 3',
#     'rang':'qora',
#     'yil':2015,
#     'narh':9000,
#     'km':89000,
#     'korobka':'mexanika'
# }
# car2 = {
#     'model':'gentra',
#     'rang':'qizil',
#     'yil':2019,
#     'narh':15000,
#     'km':20000,
#     'korobka':'mexanika'
# }
# car = car0
# print(f"{car['model'].title()},\
#       {car['rang']},\
#       {car['yil']}-yil, {car['narh']}$")

# car = car1
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")

# car = car2
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")

# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()},\
#         {car['rang']} rang,\
#         {car['yil']}-yil, {car['narh']}$")

# print(cars[0])

# print(cars[0]['rang'])

# print(f"{cars[2]['rang'].title()} "
#       f"{cars[2]['model']}")

# malibus = []
# for n in range(10):
#     new_car = {
#         'model':'malibu',
#         'rang':None,
#         'yil': 2020,
#         'narx':None,
#         'km':0,
#         'karobka':'avto'
#     }
#     malibus.append(new_car)
# for i in range(10):
#     print(malibus[i],'\n')

# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'
# for i in range(10):
#     print(malibus[i], '\n')

# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'
# for  i in range(10):
#     print(malibus[i], '\n')

# for malibu in malibus[6:]:
#     malibu['rang'] = 'qora'
#     malibu['karobka'] = 'mexanika'
# for i in range(10):
#     print(malibus[i], '\n')

# for malibu in malibus:
#     if malibu['karobka'] == 'avto':
#         malibu['narx'] = 40000
#     else:
#         malibu['narx'] = 35000

# for i in range(10):
#     print(malibus[i], '\n')

# dasturchilar = {
#     'ali':['python', 'c++'],
#     'vali':['html', 'css', 'js'],
#     'hasan':['php', 'sql'],
#     'husan':['pyhton', 'php'],
#     'maryam':['c++', 'c#']
# }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyudagi dasturlash tillarini biladi:", end = ' ')
#     for til in tillar:
#         print(til.upper(), end = ' ')

# hamkasblar = {
#     'ali' :{
#         'familiya': 'valiyev', 
#         'tyil':'1995',
#         'malumot':'oliy',
#         'tillar':['python','c++']
#     },
#         'vali': {
#         'familiya': 'aliyev', 
#         'tyil':'2001',
#         'malumot':'o\'rta maxsus',
#         'tillar':['html', 'css', 'js']
#     },
#         'hasan': {
#         'familiya': 'husanov', 
#         'tyil':'1999',
#         'malumot':'maxsus',
#         'tillar':['python','php']
#     }
# }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, \
#           {info['tyil']}-yilda tug\'ilgan. \
#             Ma\'lumoti: {info['malumot']}.\n \
#                 Quyudagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())


# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at 
# ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni 
# konsolga chiqaring.

# shaxslar = [
#     {"ism": "Abu Abdulloh Muhammad ibn Ismoil", "yil": 810, "joy": "Buxoro", "umr": 60},
#     {"ism": "Abdulla Qodiriy", "yil": 1894, "joy": "Toshkent", "umr": 44},
#     {"ism": "Erkin Vohidov", "yil": 1936, "joy": "Farg'ona", "umr": 80},
#     {"ism": "Alisher Navoiy", "yil": 1441, "joy": "Xirot", "umr": 60}
# ]

# for shaxs in shaxslar:
#     print(f"{shaxs['ism']} {shaxs['yil']}-yilda {shaxs['joy']}da tavallud topgan. {shaxs['umr']} yil umr ko'rgan.")

# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli 
# yordamida muallifning ismi va uning asarlarini konsolga chiqaring.

# shaxslar = {
#     'alisher navoiy':['xamsa', 'hayrat ul-abror', 'farhod va shirin' , 'layli va majnun'],
#     'abdulla qodiriy':['o\'tkan kunlar', 'mehrobdan chayon', 'obid ketmon'],
#     'erkin vohidov':['o\'zbegim', 'tong nafasi', 'ruhlar isyoni'],
#     'abu abdulloh muhammad ibn ismoil al-buxoriy': ['sahih al-bukhariy', 'al-adab al-mufrad']
# }
# for ism, info in shaxslar.items():
#     print(f"\n{ism} ning mashxur asarlari:")
#     for asar in info:
#         print(asar)

# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, 
# uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.

# dostlar = {
#     'Ali': ['Inception', 'The Dark Knight', 'Breaking Bad'],
#     'Vali':['Titanic', 'Avatar', 'Game of Thrones'],
#     'Hasan':['Interstellar', 'The Matrix', 'Stranger Things']
# }

# for ism, kinolar in dostlar.items():
#     print(f'\n{ism}ning sevimli kinolari:')
#     for kino in kinolar:
#         print(kino)

# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at 
# ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.

# davlatlar = {
#     'O\'zbekiston':{
#         'poytaxt':'Toshkent',
#         'aholi':36_000_000,
#         'til':'o\'zbek'
#     },
#     'AQSH':{
#         'poytaxt':'Washington',
#         'aholi':331_000_000,
#         'til':'ingliz'
#     },
#     'Yaponiya':{
#         'poytaxt':'Tokio',
#         'aholi':125_000_000,
#         'til':'yapon'
#     },
#     'Fransiya':{
#         'poytaxt':'Parij',
#         'aholi':67_000_000,
#         'til':'fransuz'
#     }
# }
# for davlat, info in davlatlar.items():
#     print(f"{davlat}ning poytaxti {info['poytaxt']}\
#           \nAholi soni: {info['aholi']}\
#           \nTil: {info['til']}\n")
    
# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi 
# so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, 
# "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.

# davlat = input('Bitta davlat kiriting:')
# info = davlatlar.get(davlat)
# if info != None:
#     print(f"{davlat}ning poytaxti {info['poytaxt']}\
#         \nAholi soni: {info['aholi']}\
#         \nTil: {info['til']}\n")
# else:
#     print('Bizda bu davlat haqida ma\'lumot yo\'q.')