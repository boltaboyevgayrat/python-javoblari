import json
import os

# Fayl nomi
file_name = "inventory.json"

# Fayl mavjudligini tekshirish va bo'sh fayl yaratish
if not os.path.exists(file_name):
    with open(file_name, 'w') as file:
        json.dump([], file)

# Mahsulotlarni chiroyli jadval ko'rinishida chiqarish funksiyasi
def view_inventory():
    with open(file_name, 'r') as file:
        inventory = json.load(file)
        if not inventory:
            print("Inventar bo'sh.")
        else:
            print(f"{'Mahsulot':<20}{'Miqdor':<10}")
            print("-" * 30)
            for item in inventory:
                print(f"{item['name']:<20}{item['quantity']:<10}")

# Yangi mahsulot qo'shish funksiyasi
def add_to_inventory():
    name = input("Mahsulot nomini kiriting: ")
    quantity = int(input("Miqdorni kiriting: "))
    with open(file_name, 'r') as file:
        inventory = json.load(file)
    inventory.append({"name": name, "quantity": quantity})
    with open(file_name, 'w') as file:
        json.dump(inventory, file, indent=4)
    print("Mahsulot muvaffaqiyatli qo'shildi!")

# Asosiy dastur
while True:
    print("\nTanlovingizni kiriting:")
    print("1. Ko'rish")
    print("2. Qo'shish")
    print("3. Chiqish")
    choice = input("Tanlov: ")

    if choice == "1":
        view_inventory()
    elif choice == "2":
        add_to_inventory()
    elif choice == "3":
        print("Dastur tugadi.")
        break
    else:
        print("Noto'g'ri tanlov, qayta urinib ko'ring.")