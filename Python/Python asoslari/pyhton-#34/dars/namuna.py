import json

x = 10
x_json = json.dumps(x)

ism = "anvar"
ism_json = json.dumps(ism)

sonlar = [12, 45, 23, 67]
sonlar_json = json.dumps(sonlar)

bemor = {
    "ism":"Alijon Valiyev",
    "yosh":30,
    "oila":True,
    "farzandlar":('Ahmad', "Bonu"),
    "allergiya":None,
    "dorilar":[
        {"nomi":"Analgin", "miqdori":0.5},
        {"nomi":"Panadol", "miqdori":1.2}
        ]
    }

bemor_json = json.dumps(bemor, indent = 4)

# print(bemor_json)

# with open("bemor.json", "w") as f:
#     json.dump(bemor, f)

sonlar1 = json.loads(sonlar_json)

bemor1 = json.loads(bemor_json)

with open("bemor.json") as f:
    bemor2 = json.load(f)
    




