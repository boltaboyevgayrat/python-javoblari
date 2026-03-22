try:
    with open('data.txt') as file:
        data = file.read()

except FileNotFoundError:
    print('Fayl mavjud emas!')
finally:
    print('Jarayon yakunlandi!')