from uuid import uuid4

class Talaba:
    """Talaba klassi"""

    __talabalar_soni = 0  # Talabalar sonini saqlash uchun klass o'zgaruvchisi
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.manzil = manzil
        self.__id = uuid4()  # Har bir talaba uchun noyob ID
        Talaba.__talabalar_soni += 1  # Har yangi talaba yaratilganda talabalar sonini oshirish

    def get_id(self):
        """Talabaning ID raqamini qaytaradi"""
        return self.__id
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"ID raqami: {self.get_id()}"
        return info
    
    @classmethod
    def get_talabalar_soni(cls):
        """Talabalar sonini qaytaradi"""
        return cls.__talabalar_soni
    
class Professor:
    """Professor klassi"""
    def __init__(self, ism, familiya, passport, tyil, fan, lavozim):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.fan = fan
        self.lavozim = lavozim

    def get_fan(self):
        """Professorning o'qitadigan fanini qaytaradi"""
        return self.fan
    
    def get_info(self):
        """Professor haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Fan: {self.get_fan()}"
        return info
    
class Foydalanuvchi:
    """Foydalanuvchi klassi"""
    def __init__(self, ism, familiya, passport, tyil, username, password):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.username = username
        self.password = password

    def get_username(self):
        """Foydalanuvchining username'ini qaytaradi"""
        return self.username
    
    def get_info(self):
        """Foydalanuvchi haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Username: {self.get_username()}"
        return info
    
class Shaxs:
    """Shaxs klassi"""
    odamlar_soni = 0  # Shaxslar sonini saqlash uchun klass o'zgaruvchisi
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__id = uuid4()  # Har bir shaxs uchun noyob ID
        Shaxs.odamlar_soni += 1  # Har yangi shaxs yaratilganda odamlar sonini oshirish

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport: {self.passport}"
        return info
    
    def get_id(self):
        """Shaxsning ID raqamini qaytaradi"""
        return self.__id
    
    @classmethod
    def get_odamlar_soni(cls):
        """Shaxslar sonini qaytaradi"""
        return cls.odamlar_soni