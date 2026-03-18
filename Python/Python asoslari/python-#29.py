# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1

#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi method"""
#         self.bosqich = bosqich

#     def update_bosqich(self):
#         """Talabaning bosqichini 1 taga ko'paytirish"""
#         self.bosqich += 1

#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
    
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
    
#     def get_fullname(self):
#         """Talabaning to'liq ismini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
    
#     def get_age(self, yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil - self.tyil
    
# talaba1 = Talaba("Alijon", "Valiyev", 2000)
# print(talaba1.get_info())

# talaba1.bosqich = 2
# print(talaba1.get_info())

# talaba1.set_bosqich(3)
# print(talaba1.get_info())

# talaba1.update_bosqich()
# print(talaba1.get_info())

# class Fan():
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []

#     def add_student(self, talaba):
#         """Fanga talaba qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1

#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]
    
#     def get_name(self):
#         """Fan nomi"""
#         return self.nomi
    
#     def get_students_num(self):
#         """Fanga yozilgan talabalar soni"""
#         return self.talabalar_soni
    
    
# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Alijon","Valiyev",2000)
# talaba2 = Talaba("Hasan","Alimov",2001)
# talaba3 = Talaba("Akrom","Boriyev",2001)

# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# print(matematika.talabalar_soni)

# print(matematika.talabalar)

# print(matematika.get_students())

# print(dir(Talaba))

# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(Talaba))

# print(see_methods(talaba1))

# print(talaba1.__dict__)

# print(talaba1.__dict__.keys())

# class Avto:
#     def __init__(self, model, rang, korobka, narh, yil, km=0):
#         self.model = model          # mashina modeli
#         self.rang = rang            # rangi
#         self.korobka = korobka      # mexanik / avtomat
#         self.narh = narh            # narxi
#         self.yil = yil              # ishlab chiqarilgan yili
#         self.km = km                # yurgan masofa (standart = 0)

#     def info(self):
#         return f"{self.yil}-yil {self.model}, {self.rang}, {self.korobka}, {self.km} km, {self.narh}$"

#     def update_km(self, yangi_km):
#         if yangi_km >= self.km:
#             self.km = yangi_km
#         else:
#             print("Kilometrni kamaytirib bo'lmaydi!")

# avto1 = Avto("Chevrolet Malibu", "qora", "avtomat", 25000, 2022)
# avto2 = Avto("Toyota Camry", "oq", "avtomat", 30000, 2023, 10000)
# avto3 = Avto("Nexia 3", "kulrang", "mexanik", 12000, 2021)

# print(avto1.info())
# print(avto2.info())
# print(avto3.info())

# class Avtosalon:
#     def __init__(self, nomi, manzil):
#         self.nomi = nomi                  # salon nomi
#         self.manzil = manzil              # salon manzili
#         self.avtomobillar = []            # sotuvdagi mashinalar ro'yxati

#     def avto_qoshish(self, avto):
#         self.avtomobillar.append(avto)

#     def avto_info(self):
#         for avto in self.avtomobillar:
#             print(avto.info())

#     def jami_avto_soni(self):
#         return len(self.avtomobillar)
    
# salon = Avtosalon("Premium Avto", "Toshkent")

# Mashinalarni qo‘shamiz
# salon.avto_qoshish(avto1)
# salon.avto_qoshish(avto2)
# salon.avto_qoshish(avto3)

# salon.avto_info()
# print("Jami avtomobillar soni:", salon.jami_avto_soni())

# print(dir(Avto))

# print(dir(str))

# print(dir(int))

# print(Avto.__dict__)