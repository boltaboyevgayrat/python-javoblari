import json

with open('telefonlar.json') as file:
    telefonlar = json.load(file)


narx = []
for telefon in telefonlar:
    narx.append(telefon['narx'])
    
for index in range(len(narx)):
    if min(narx) == narx[index]:
        print(telefonlar[index])
        break
    