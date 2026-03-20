# from uuid import uuid4
# class Avto:
#     """Avtombil klassi"""
#     __num_avto = 0
    
#     def __init__(self, make, model, rang, yil, narh, km = 0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1

#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_avto
    
#     def __repr__(self):
#         """Obyekt haqida ma'lumot"""
#         return f"Avto: {self.rang} {self.make} {self.model}"
    
#     def __eq__(self, boshqa_avto):
#         """Tenglik"""
#         return self.narh == boshqa_avto.narh
    
#     def __lt__(self, boshqa_avto):
#         """Kichik"""
#         return self.narh < boshqa_avto.narh
    
#     def __le__(self, boshqa_avto):
#         """Kichik yoki teng"""
#         return self.narh <= boshqa_avto.narh
    
# # print(dir(Avto))

# avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
# avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)
# avto3 = Avto("Toyota", "Carolla", "Silver", 2018, 45000)
# avto4 = Avto("Mazda", "6", "Qizil", 2015, 35000)
# avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
# avto6 = Avto("Honda","Accord","Oq",2017,42000)



# # print(avto1)

# # print(avto1 > avto2)

# class Avtosalon:
#     """Avtosalon klassi"""
#     def __init__(self, name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         return f"{self.name} avtosaloni"
    
#     # def add_avto(self, *avto):
#     #     if isinstance(avto, Avto):
#     #         self.avtolar.append(avto)
#     #     else:
#     #         print("Avto obyektini kiriting")
    

            
#     def __len__(self):
#         return len(self.avtolar)
    
#     def __getitem__(self, index):
#          return self.avtolar[index]
     
#     def __setitem__(self, index, value):
#         if isinstance(value, Avto):
#             self.avtolar[index] = value
#     def add_avto(self, *qiymat):
#         for avto in qiymat:
#             if isinstance(avto, Avto):
#                 self.avtolar.append(avto)
#             else:
#                 print("Avto obyektini kiriting")
                
#     def __add__(self, qiymat):
#         if isinstance(qiymat, Avtosalon):
#             yangi_salon = Avtosalon(f"{self.name} {qiymat.name}")
#             yangi_salon.avtolar = self.avtolar + qiymat.avtolar
#             return yangi_salon
#         elif isinstance(qiymat, Avto):
#             self.add_avto(qiymat)
#         else:
#             print(f"Avtosalonga {type(qiymat)} qo'shib bo'lmaydi")
            
#     def __call__(self, *param):
#         if param:
#             for avto in param:
#                 self.add_avto(avto)
#         else:
#             return [avto for avto in self.avtolar]
            

        
    

# salon1 = Avtosalon("MaxAvto")
# salon2 = Avtosalon("Avto Lider")

# salon1.add_avto(avto1,avto2, avto3)
# salon2.add_avto(avto4, avto5, avto6)

# avto7 = Avto("BMW", 'X7','Qora',2015,75000)
# avto_new = Avto("Mercedes-Benz", 'E200','Silver',2015,80000)
# salon1(avto_new) # Yangi avto qo'shamiz
# print(salon1()) # salondagi mashinalarni ko'ramiz

class Shaxs:
    """Shaxs klassi"""
    def __init__(self, ism, familiya, passport):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport

    def __repr__(self):
        return f"{self.ism} {self.familiya}"
    
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, id):
        super().__init__(ism, familiya, passport)
        self.id = id
        self.bosqich = 1

    def add_bosqich(self):
        self.bosqich += 1

    def __lt__(self, boshqa_talaba):
        return self.bosqich < boshqa_talaba.bosqich
    
    def __eq__(self, boshqa_talaba):
        return self.bosqich == boshqa_talaba.bosqich
    
    def __le__(self, boshqa_talaba):
        return self.bosqich <= boshqa_talaba.bosqich

shaxs1 = Shaxs("Ali", "Valiyev", "AA1234567")
talaba1 = Talaba("Vali", "Aliyev", "BB1234567", 1232423)
talaba1.add_bosqich()
talaba2 = Talaba("Gulnora", "Karimova", "CC1234567", 1232424)
talaba3 = Talaba("Sardor", "Rashidov", "DD1234567", 1232425)
talaba4 = Talaba("Diyor", "Shomurodov", "EE1234567", 1232426)
talaba5 = Talaba("Jasur", "Abdullayev", "FF1234567", 1232427)
talaba6 = Talaba("Nodir", "Shomurodov", "GG1234567", 1232428)

class Fan:
    """Fan klassi"""
    def __init__(self, name):
        self.name = name
        self.talabalar = []

    def add_talaba(self, *talaba):
        for t in talaba:
            if isinstance(t, Talaba):
                self.talabalar.append(t)
            else:
                print("Talaba obyektini kiriting")

    def __repr__(self):
        return f"{self.name} fani"
    def __getitem__(self, index):
        return self.talabalar[index]
    def __setitem__(self, index, value):
        if isinstance(value, Talaba):
            self.talabalar[index] = value
        else:
            print("Talaba obyektini kiriting")

    def __len__(self):
        return len(self.talabalar)
    
    def __add__(self, boshqa_fan):
        if isinstance(boshqa_fan, Fan):
            yangi_fan = Fan(f"{self.name} va {boshqa_fan.name}")
            yangi_fan.talabalar = self.talabalar + boshqa_fan.talabalar
            return yangi_fan
        elif isinstance(boshqa_fan, Talaba):
            self.add_talaba(boshqa_fan)
        else:
            print("Faqat fan obyektini qo'shish mumkin")

    def __call__(self, *talaba):
        if talaba:
            for t in talaba:
                self.add_talaba(t)
        else:
            return [t for t in self.talabalar]
        
    def __sub__(self, talaba_id_or_talaba_passport):
        if isinstance(talaba_id_or_talaba_passport, int):
            for t in self.talabalar:
                if t.id == talaba_id_or_talaba_passport:
                    self.talabalar.remove(t)
                    break
        elif isinstance(talaba_id_or_talaba_passport, str):
            for t in self.talabalar:
                if t.passport == talaba_id_or_talaba_passport:
                    self.talabalar.remove(t)
                    break
        else:
            print("Talaba ID yoki passport raqamini kiriting")

fan1 = Fan("Matematika")
fan2 = Fan("Fizika")
fan1.add_talaba(talaba1, talaba2, talaba3)
fan2.add_talaba(talaba4, talaba5, talaba6)









        

