# filename = "data/pi_million_digits.txt"
# with open(filename) as file:
#     pi = file.read()

# pi = pi.rstrip()
# pi = pi.replace("\n", "")
# while True:
#     tugilgan_kun = input("Tug'ilgan kuningizni kiriting (DDMMYYYY formatida): ")
#     if len(tugilgan_kun) != 8:
#         print("Iltimos, tug'ilgan kuningizni to'g'ri formatda kiriting (DDMMYYYY)")
#         continue
#     elif not tugilgan_kun.isdigit():
#         print("Iltimos, faqat raqamlarni kiriting (DDMMYYYY formatida)")
#         continue
#     else:
#         pi.find(tugilgan_kun)
#         if pi.find(tugilgan_kun) != -1:
#             print(f"Tabriklaymiz! {tugilgan_kun} soni pi ning {pi.find(tugilgan_kun)}-raqamidan keyin keladi.")
#         else:
#             print(f"Kechirasiz, {tugilgan_kun} soni pi ning bir million raqamida topilmadi.")

#     xabar = input("Yana bir marta tekshirishni xohlaysizmi? (ha/yo'q): ")
#     if xabar.lower() != "ha":
#         print("Dastur tugadi. Yana ko'rishguncha!")
#         break  
#   
def malumot_yozish():
    with open("data/malumotlar.txt", "a") as fayl:
        while True:
            malumot = input("Ma'lumot kiriting (to'xtatish uchun 'stop'): ")
            
            if malumot.lower() == "stop":
                print("Dastur to'xtadi.")
                break
            
            fayl.write(malumot + "\n")

malumot_yozish()