# class Shaxs:
#     """Shaxs haqida ma'lumot"""
#     def __init__(self, ism, familiya, passport, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil

#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}.\nPassport:{self.passport} \n{self.tyil}-yilda tug'ilgan"
    
#     def get_name(self):
#         """Shaxsning ismini qaytaradi"""
#         return self.ism
    
#     def get_lastname(self):
#         """Shaxsning familiyasini qaytaradi"""
#         return self.familiya
    
#     def get_fullname(self):
#         """Shaxsning to'liq ismini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
    
#     def get_age(self, yil):
#         """Shaxsning yoshini qaytaradi"""
#         return yil - self.tyil
    
# inson = Shaxs("Alimov", "Hasan", "FB001122", 2006)
# print(f"{inson.get_info()}. {inson.get_age(2026)} yoshda.")

# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil = manzil
#         self.fanlar = []

#     def get_id(self):
#         """Talabaning id raqamini qaytaradi"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning bosqichini qaytaradi"""
#         return self.bosqich
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info
    
#     def fanga_yozil(self, fan):
#         """Fanga yozil"""
#         self.fanlar.append(fan)

#     def remove_fan(self, fan):
#         """Fanni o'chir"""
#         if fan in self.fanlar:
#             self.fanlar.remove(fan)
#         else:
#             return "Bu fanga yozilmagansiz."
    
# class Manzil:
#     """Manzil saqlash uchun klass"""
#     def __init__(self, uy, kocha, tuman, viloyat):
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat

#     def get_manzil(self):
#         """Manzilni ko'rish"""
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha}, {self.uy}-uy"
#         return manzil
    

        


# talaba1 = Talaba("Valijon", "Aliyev", "FA112299", 2000, "0000011")
# print(talaba1.get_info())

# print(talaba1.get_age(2026))

# print(f"{talaba1.get_info()}. ID raqami:{talaba1.get_id()}")

# print(talaba1.get_info())

# talaba_manzili = Manzil(12, "Olmazor", "Bog'bon", "Samarqand")

# talaba = Talaba("Valijon", "Aliyev", "FA112299", 2000, "0000012", talaba_manzili)

# print(talaba.manzil.get_manzil())

# print(talaba.manzil.tuman)

# class Fan:
#     """Fanlarni saqlash uchun klass"""
#     def __init__(self, fan):
#         self.fan = fan
    
# matematika = Fan("Matematika") 
# geografiya = Fan("Geografiya")
# biologiya = Fan("Biologiya")

# class Professor(Shaxs):
#     """Professor klassi"""
#     def __init__(self, ism, familiya, passport, tyil, fan):
#         super().__init__(ism, familiya, passport, tyil)
#         self.fan = fan

#     def get_fan(self):
#         """Professorning fanini qaytaradi"""
#         return self.fan
    
#     def get_info(self):
#         """Professor haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_fan()} fani bo'yicha professor."
#         return info
    
# class Foydalanuvchi(Shaxs):
#     """Foydalanuvchi klassi"""
#     def __init__(self, ism, familiya, passport, tyil, username, password):
#         super().__init__(ism, familiya, passport, tyil)
#         self.username = username
#         self.password = password

#     def get_username(self):
#         """Foydalanuvchining username'ini qaytaradi"""
#         return self.username
    
#     def get_password(self):
#         """Foydalanuvchining password'ini qaytaradi"""
#         return self.password
    
#     def get_info(self):
#         """Foydalanuvchi haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Username: {self.username}"
#         return info
    
# class Sotuvchi(Shaxs):
#     """Sotuvchi klassi"""
#     def __init__(self, ism, familiya, passport, tyil, dokon_nomi):
#         super().__init__(ism, familiya, passport, tyil)
#         self.dokon_nomi = dokon_nomi

#     def get_info(self):
#         """Sotuvchi haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.dokon_nomi} do'konining sotuvchisi."
#         return info

# class Mijoz(Shaxs):
#     """Mijoz klassi"""
#     def __init__(self, ism, familiya, passport, tyil, mijoz_id):
#         super().__init__(ism, familiya, passport, tyil)
#         self.mijoz_id = mijoz_id

#     def get_info(self):
#         """Mijoz haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Mijoz ID: {self.mijoz_id}"
#         return info
    
# class Admin(Foydalanuvchi):
#     """Admin klassi"""
#     def __init__(self, ism, familiya, passport, tyil, username, password, admin_id):
#         super().__init__(ism, familiya, passport, tyil, username, password)
#         self.admin_id = admin_id

#     def get_info(self):
#         """Admin haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Admin ID: {self.admin_id}"
#         return info
    
#     def ban_user(self, foydalanuvchi):
#         """Foydalanuvchini ban qilish"""
#         return f"{foydalanuvchi.get_username()} foydalanuvchisi ban qilindi."
    
# # Admin va Foydalanuvchi klasslarini ishlatish

# # Foydalanuvchi obyektini yaratish
# foydalanuvchi1 = Foydalanuvchi("Ali", "Valiyev", "AA123456", 1995, "ali95", "password123")

# # Admin obyektini yaratish
# admin1 = Admin("Hasan", "Karimov", "BB654321", 1990, "admin_hasan", "adminpass", "A001")

# # Foydalanuvchi haqida ma'lumot
# print(foydalanuvchi1.get_info())

# # Admin haqida ma'lumot
# print(admin1.get_info())

# # Foydalanuvchini ban qilish
# print(admin1.ban_user(foydalanuvchi1))