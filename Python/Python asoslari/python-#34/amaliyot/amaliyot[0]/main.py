import json

# Bizning ma'lumotlarimiz (Python lug'ati)
kutubxona = {
    "nomi": "Markaziy Kutubxona",
    "manzil": "Toshkent sh., Amir Temur ko'chasi",
    "kitoblar": [
        {"id": 1, "nom": "O'tkan kunlar", "muallif": "Abdulla Qodiriy", "yil": 1922},
        {"id": 2, "nom": "Sariq devni minib", "muallif": "Xudoyberdi To'xtaboyev", "yil": 1968},
        {"id": 3, "nom": "Python asoslari", "muallif": "Guido van Rossum", "yil": 1991}
    ]
}

# Ma'lumotni JSON faylga yozish
with open("kitoblar.json", "w", encoding="utf-8") as fayl:
    # indent=4 - chiroyli ko'rinish uchun, ensure_ascii=False - o'zbekcha harflar buzilmasligi uchun
    json.dump(kutubxona, fayl, indent=4, ensure_ascii=False)

print("Ma'lumotlar 'kitoblar.json' fayliga muvaffaqiyatli saqlandi!")

# Fayldan o'qish
with open("kitoblar.json", "r", encoding="utf-8") as fayl:
    yuklangan_malumot = json.load(fayl)

# Keling, faqat kitoblar ro'yxatini va ularning nomlarini chiqaramiz
print(f"\nKutubxona: {yuklangan_malumot['nomi']}")
print("-" * 30)

# for kitob in yuklangan_malumot["kitoblar"]:
#     print(f"ID: {kitob['id']} | Kitob: {kitob['nom']} | Muallif: {kitob['muallif']}")

def add_book(name, muallif, yil):
    id_raqam = kutubxona['kitoblar'][-1]['id']
    yangi_dict = {
        'id':id_raqam + 1,
        'nom':name,
        'muallif':muallif,
        'yil':yil
        }
    kutubxona['kitoblar'].append(yangi_dict)
    with open("kitoblar.json", "w", encoding="utf-8") as fayl:
        # indent=4 - chiroyli ko'rinish uchun, ensure_ascii=False - o'zbekcha harflar buzilmasligi uchun
        json.dump(kutubxona, fayl, indent=4, ensure_ascii=False)

    