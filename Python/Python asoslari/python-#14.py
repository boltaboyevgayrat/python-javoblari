# 3/4/2026
#  #14 LUG'AT BILAN TANISHUV

# #Keling, sodda lug'at yaratamiz:
# car_0 = {'model':'ferrari','rang':qizil}

# #  Lug'atdagi biror qiymatni ko'rish uchun unga kalit so'z orqali murojat qilamiz:
# car_0 = {'model':'ferrari','rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

# # Lug'atdagi qiymatlar son (int, float), matn (string), ro'yxat (list, tuple) va hatto boshqa lug'at ham bo'lishi mumkin.
# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#     {talaba_0['t_yil']}-yilda tu'gilgan,\
#     {talaba_0['yosh']} yoshda")

#  yuqoridagi talaba_0 nomli lu'gatga yana 2 ta yangi, kurs va fakultet nomli, kalit so'zlar va qiymatlar qo'shamiz:
# talaba_0['kurs'] = 4 # yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
# talaba_0['fakultet'] = 'informatika' # 'fakultet' ga esa 'informatika' 
# print(talaba_0)

# # Bo'sh lug'at yaratish:
# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# talaba_0 = {'ism':'murod olimov','yosh':20, 't_yil': 2000}
# print(talaba_0)
# del talaba_0['yosh']
# print(talaba_0)

# telefonlar = {
#     'ali':"iphone x",
#     'vali':'galaxy s9',
#     'olim': 'mi 10 pro',
#     'orif':'nokia 3310'
# }
# phone = telefonlar['ali']
# print(f"Alining telefoni {phone}")

# phone = telefonlar['hasan']
# print(f"Hasanning telefoni {phone}")

# phone = telefonlar.get('hasan', 'Bunday ism mavjud emas.')
# print(phone)

# phone = telefonlar.get('hasan')
# print(phone)


# # otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta
# # m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida
# # konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
# otam = {
#     'ism':'orifjon',
#     't_yili': 1979,
#     'shahar':'Qoraqolpog\'iston respublikasi'
# }
# print(f"Otamning ismi {otam['ism'].title()}, {otam['t_yili']}-yilda, {otam['shahar']}da tug'ilgan.")


# # Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi 
# # bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
# taomlar = {
#     'dadam':'osh',
#     'oyim':'manti',
#     'ukam':'bo\'rak',
#     'singlim':'somsa',
#     'men':'shashlik'
# }
# print(f"Dadamning sevimli taomi {taomlar['dadam']}.")
# print(f"Ukamning sevimli taomi {taomlar['ukam']}.")
# print(f"Mening sevimli taomim {taomlar['men']}.")



# # Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting
# # (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
# atamalar = {
#     'integer':'butun son',
#     'float': 'o\'lik son',
#     'string': 'matn',
#     'if':'agar',
#     'else':'aks holda',
#     'print':'chop etish',
#     'bool':'mantiqiy element',
#     'elif':'else if birgalikda',
#     'list':'ro\'yxat',
#     'tuple':'o\'zgarmas ro\'yxat'
# }


# # Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib 
# # bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
# print(atamalar.get(input('Kalit so\'z kiriting: '), 'Bunday so\'z mavjud emas.'))

# # Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli 
# # ko'rinishda chiqaring.
# kiritish = input('Kalit so\'z kiriting: ')
# key = atamalar.get(kiritish)

# if key == None:
#     print('Bunday so\'z mavjud emas.')
# else:
#     print(f"{kiritish.title()} so\'zi {key.title()} deb tarjima qilinadi.")