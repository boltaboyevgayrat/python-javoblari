# x = 10
# print(type(x))

# matn = 'salom'

# print(type(matn))

# def salom_ber():
#     print('Assalomu alaykum')

# print(type(salom_ber))

# matn = 'salom'

# print(matn.upper())
# son  = 10
# son.upper()

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil

#     def tanishtir(self):
#         print(f'Ismim {self.ism} {self.familiya}. {self.tyil} yilda tug\'ilganman.')

#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
#     def get_fullname(self):
#         """Talabaning to\'liq ismini qaytaradi"""
#         return f'{self.ism} {self.familiya}'
    
#     def get_age(self, yil):
#         "Talabaning yoshini qaytaradi"
#         return yil - self.tyil
# class User:
#     def __int__(self,name,username,email):
#         self.name = name
#         self.uname = username
#         self.mail = email
    
#     def describe():
#         pass
    
#     def get_email():
#         pass
    

# talaba1 = Talaba('Alijon', 'Valiyev', 2000)
# print(talaba1.ism)

# print(talaba1.familiya)
# talaba2 = Talaba('Olim', 'Olimov', 1995)
# talaba3 = Talaba('Husan', 'Akbarov', 2004)
# talaba4 = Talaba('Hasan', 'Akbarov', 2004)

# print(talaba2.ism)
# print(talaba4.familiya)

# talaba4.tanishtir()

# print(talaba1.get_fullname())

# print(talaba1.get_age(2026))

# class User:
#     def __init__(self, ism, familiya, username, email, parol):
#         self.ism = ism
#         self.familiya = familiya
#         self.username = username
#         self.email = email
#         self.parol = parol

#     def get_info(self):
#         """Foydalanuvchi haqida ma'lumot qaytaradi"""
#         return f"Ism: {self.ism}, Familiya: {self.familiya}, Username: {self.username}, Email: {self.email}"


# # Klassdan foydalanish
# user1 = User("G'ayrat", "Boltaboyev", "gayrat01", "gayrat@gmail.com", "12345")

# print(user1.get_info())