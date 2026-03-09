# ismlar = []

# print('Yaqin do\'stlaringiz ro\'yxatini tuzamiz.')
# n = 1
# while True:
#     savol = f'{n}-do\'stingiz ismini kiriting: '
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input('Yana ism qo\'shasizmi? (ha/yo\'q) ')
#     if javob == 'ha':
#         n += 1
#         continue
#     else:
#         break

# print('Do\'stlaringiz yo\'yxati:')
# for ism in ismlar:
#     print(ism.title())

# print('Do\'stlaringiz yoshini saqlaymiz.')
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input('Do\'stingiz ismini kiriting: ')
#     yosh = input(f'{ism.title()}ning yoshini kiriting: ')
#     dostlar[ism] = int(yosh)

#     javob = input('Yana ma\'lumot qo\'shasizmi? (ha/yo\'q): ')
#     if javob == 'yo\'q':
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f'{ism.title()} {yosh} yoshda.')

# cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)

# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = int(input(f'{talaba.title()}ning bahosini kiriting: '))
#     print(f'{talaba.title()} baholandi.')
#     baholangan_talabalar[talaba] = baho

# print(baholangan_talabalar)

# javob = input('Buyurtma berasizmi? (ha/yo\'q) ')
# buyurtmalar = []
# while True:
#     if javob != 'ha':
#         break
#     buyurtma = input('Buyurmani nomini yozing: ')
#     buyurtmalar.append(buyurtma)
#     javob = input('Buyurtma berasizmi? (ha/yo\'q) ')

# print(buyurtmalar)

# E-bozor mahsulotlari lug'ati
# mahsulotlar = {}

# while True:
#     nom = input("Mahsulot nomini kiriting (to'xtatish uchun 'stop' yozing): ")
    
#     if nom.lower() == "stop":
#         break
    
#     narx = float(input(f"{nom} narhini kiriting: "))
#     mahsulotlar[nom] = narx

# print("\nE-bozor mahsulotlari:")
# for nom, narx in mahsulotlar.items():
#     print(nom, "->", narx, "so'm")

# # 1. Buyurtmalar ro'yxati
# buyurtma = []

# while True:
#     mahsulot = input("Buyurtma mahsulotini kiriting (stop - tugatish): ")
#     if mahsulot.lower() == "stop":
#         break
#     buyurtma.append(mahsulot)

# # 2. E-bozor mahsulotlari va narxlari
# bozor = {}

# while True:
#     nom = input("Bozordagi mahsulot nomini kiriting (stop - tugatish): ")
#     if nom.lower() == "stop":
#         break
#     narx = float(input(f"{nom} narhini kiriting: "))
#     bozor[nom] = narx

# # 3. Buyurtmani tekshirish
# print("\nBuyurtma natijasi:")
# for mahsulot in buyurtma:
#     if mahsulot in bozor:
#         print(mahsulot, "narxi:", bozor[mahsulot], "so'm")
#     else:
#         print(mahsulot, "- Bizda bu mahsulot yo'q")