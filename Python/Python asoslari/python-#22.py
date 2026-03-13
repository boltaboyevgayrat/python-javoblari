# def summa(*sonlar):
#     """Kiritilgan sonlarning yig\'indisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(1, 2))
# print(summa(1, 2, 3, 4, 5))

# def summa(*sonlar):
#     """Kiritilgan sonlarning yig\'indisini hisoblaydigan funksiya"""
#     return sum(sonlar)

# print(summa(1, 2))
# print(summa(4, 5, 6, 7))

# def summa(x, y, *sonlar):
#     """Kiritilgan sonlarning yig'indisini hisoblaydigan funksiya"""
#     return x + y + sum(sonlar)
# print(summa(1, 2))
# print(summa(1, 2, 3, 4, 5))
# print(summa(4, 5, 6, 7))
# print(summa(2))

# def avto_info(kompaniya, model, **malumotlar):
#     """Avto haqida ma\'lumotlarni lug\'at ko\'rinishida qaytaruvchi funksiya"""
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar

# avto1 = avto_info('GM', 'malibu', rang = 'qora', yil = 2018)
# avto2 = avto_info('Kia', 'K5', rang = 'qizil', narh = 35000)

# print(avto1)
# print(avto2)

# def kopaytma(*sonlar):
#     """Kiritilgan sonlarning ko\'paytmasini hisoblaydigan funksiya"""
#     kopaytma = 1
#     for son in  sonlar:
#         kopaytma *= son
#     return kopaytma

# print(kopaytma(3, 5, 7))

# def talaba_info(ism, familiya, **malumotlar):
#     malumotlar['ism'] = ism
#     malumotlar['familiya'] = familiya
#     return malumotlar
# talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT')
# print(talaba)