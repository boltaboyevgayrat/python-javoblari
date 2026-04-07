import json

json_kurs = '{"valyuta": "USD", "kurs": 12650, "sana": "2026-03-21"}'

kurs = json.loads(json_kurs)


while True:
    summa = int(input("Summani kiriting:  "))
    usd = summa / kurs['kurs']
    print(usd)
    
    xabar = input("Yana summa kiritasizmi (ha/yo'q)?  ")
    if xabar != 'ha':
        break

print("Dastur tugadi!")