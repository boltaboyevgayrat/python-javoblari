import json



new_list = []

def add_user(name, age, color):
    new_dict = {
        "name":name,
        "age": age,
        'fav_color': color
        }
    new_list.append(new_dict)
    with open("profil.json", "w") as file:
        json.dump(new_list, file)
        
while True:
    ism = input("Ismingizni kiriting:  ")
    yosh = int(input("Yoshingizni kiriting:  "))
    rang = input("Sevimli rangingizni kiriting:  ")
    add_user(ism, yosh, rang)
    xabar = input("Yana foydalsnuvchi kiritasizmi (ha/yo'q)?  ")
    if xabar != "ha":
        break
