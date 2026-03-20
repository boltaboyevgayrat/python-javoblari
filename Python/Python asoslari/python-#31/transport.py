from uuid import uuid4

class Avto:
    """Avtombil klassi"""
    __num_avto = 0
    
    def __init__(self, make, model, rang, yil, narh, km = 0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    
class Bus(Avto):
    """Avtobus klassi"""
    def __init__(self, make, model, rang, yil, narh, km = 0, yoqilgi = "dizel", oturadigan_joy = 50):
        super().__init__(make, model, rang, yil, narh, km)
        self.yoqilgi = yoqilgi
        self.oturadigan_joy = oturadigan_joy

class Train(Avto):
    """Poyezd klassi"""
    def __init__(self, make, model, rang, yil, narh, km = 0, yoqilgi = "elektr", vagon_soni = 10):
        super().__init__(make, model, rang, yil, narh, km)
        self.yoqilgi = yoqilgi
        self.vagon_soni = vagon_soni

