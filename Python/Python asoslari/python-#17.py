# ism = input('Ismingiz nima? >>')
# print(f'salom, {ism}')

# ism = input('ismingiz nima? >>')
# savol = f'Salom {ism}, yoshingiz nechchida? >>'
# yosh = input(savol)

# ism = input('Ismingiz nima? >>')
# savol = f'Salom {ism}, yoshingiz nechchida? >>'
# yosh = input(savol)
# yosh = int(yosh)
# height = input('Bo\'yingiz nechchi metr? >>')
# height = float(height)

# son = 1
# while son <= 5:
#     print(son, end=' ')
#     son += 1

# print('Kiritilgan sonning kvadratini hisoblovchi dastur.')
# savol = 'Istalgan son kiriting'
# savol += '(dasturni to\'xtatish uchun "exit" deb yozing)'
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

# print('Kiritilgan sonning kvadratini hisoblovchi dastur.')
# savol = 'Istalgan son kiriting'
# savol += '(dasturni to\'xtatish uchun "exit" deb yozing)'
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)


# print('Kiritilgan sonning kvadratini hisoblovchi dastur.')
# savol = 'Istalgan son kiriting'
# savol += '(dasturni to\'xtatish uchun "exit" deb yozing)'
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)

# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         break
#     else:
#         print(f'{son} ning kvadrati {son**2} ga teng.')

# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f'{son} ning kvadrati {son**2} ga teng.')

# son = 0
# while son < 10:
#     son += 1
#     if son % 2 != 0:
#         continue
#     print(son)

# son = 0
# while son < 10:
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)

# son = 0
# while son < 10:
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)
#     son += 1

# son = 1
# while son > 0:
#     son += 1
#     if son % 2  != 0:
#         continue
#     else:
#         print(son)

# kitoblar = []
# qiymat = ''
# while True:
#     qiymat = input('Sevimli kitoblaringizni kiritng(Agar dasturni to\'xtatmoqchi bo\'lsangiz "stop" deb yozing)')
#     if qiymat == 'stop':
#         break
#     kitoblar.append(qiymat)
# print('Sizning sevimli kitoblariz ro\'yxati:\n', kitoblar)

# while True:
#     yosh = input('Yoshingizni kiriting(Agar dasturni to\'xtatmoqchi bo\'lsangiz "stop" yoki "exit" deb yozing)')
#     if yosh == 'stop' or yosh == 'exit':
#         break
#     elif int(yosh) < 7:
#         print('2000 so\'m')
#     elif int(yosh) >= 7 and int(yosh) < 18:
#         print('3000 so\'m')
#     elif int(yosh) >= 18 and int(yosh) < 65:
#         print('10000 so\'m')
#     else:
#         print('Sizga chipta tekin.')

# ishora = True
# while ishora:
#     yosh = input('Yoshingizni kiriting(Agar dasturni to\'xtatmoqchi bo\'lsangiz "stop" yoki "exit" deb yozing)')
#     if yosh == 'stop' or yosh == 'exit':
#         ishora = False
#     elif int(yosh) < 7:
#         print('2000 so\'m')
#     elif int(yosh) >= 7 and int(yosh) < 18:
#         print('3000 so\'m')
#     elif int(yosh) >= 18 and int(yosh) < 65:
#         print('10000 so\'m')
#     else:
#         print('Sizga chipta tekin.')

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")