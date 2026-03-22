import json

# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

# data_json = json.dumps(data)

# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""

# talaba = json.loads(talaba_json)

# with open("talaba.json", "w") as f:
#     json.dump(talaba, f)
    
# with open("data.json", "w") as f:
#     json.dump(data, f)
    
# with open("students.json") as f:
#     talabalar = json.load(f)
    
    
# for talaba in talabalar["student"]:
#     print(f"{talaba['name'].title()} {talaba['lastname']}, {talaba['year']}-kurs, {talaba['faculty']} talabasi")
    
with open("api-result.json") as f:
    python = json.load(f)

print(python['query']['pages']['13801']['title'])

print(python['query']['pages']['13801']['extract'])
