import json

def kitoblar_json_saqlash_va_oqish():
    # Kitoblar ro'yxati
    kitoblar = [
        {"nomi": "Python", "muallif": "Guido"},
        {"nomi": "Algoritmlar", "muallif": "Robert"}
    ]

    # Ro'yxatni JSON formatida saqlash
    with open('data/data.json', 'w') as fayl:
        json.dump(kitoblar, fayl, indent=4)

    # JSON faylni qayta o'qish
    with open('data/data.json', 'r') as fayl:
        yuklangan_kitoblar = json.load(fayl)

    # Kitoblarni chiroyli qilib ekranga chiqarish
    for kitob in yuklangan_kitoblar:
        print(f"Kitob nomi: {kitob['nomi']}, Muallif: {kitob['muallif']}")

