def avto_info(kompaniya, model, rang, karobka, yili, narhi = None):
    """Avtomobil haqidagi ma\'lumotlarni lug\'at ko\'rinishida qaytaruvchi funksiya"""
    avto = {
        'kompaniya':kompaniya,
        'model':model,
        'rang': rang,
        'karobka': karobka,
        'yil': yili,
        'narh':narhi
    }
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma\'lumotlarni bitta ro\'yhatga joylash imkonini beruvchi funksiya"""
    avtolar = []
    while True:
        print('\nQuyudagi ma\'lumotlarni kiriting', end = '')
        kompaniya = input('Ishlab chiqaruvchi: ')
        model = input('Model: ')
        rangi = input('Rangi: ')
        karobka = input('Karobka: ')
        yili = int(input('Ishlab chiqarilgan yili: '))
        narhi = float(input('Narhi: '))

        avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))

        javob = input('Yana avto qo\'shasizmi? (yes/no): ')
        if javob == 'no':
            break
    return avtolar

def info_print(avto_info):
    """Avtomobil haqida ma\'lumotlar saqlangan lug\'atni konsolga chiqaruvchi funksiya"""
    print(f'{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} '
          f'{avto_info['model'].upper()}, {avto_info['karobka']} karobka, '
          f'{avto_info['yil']}-yil, {avto_info['narh']}$')