import pickle

# with open("pi.txt") as file:
#     pi = file.read()
    
# pi = pi.rstrip()
# pi = pi.replace("\n", "")
# pi = float(pi)
# print(pi)

# filename = "data/talabalar.txt"
# with open(filename) as file:
#     for line in file:
#         print(line)

# filename = "data/talabalar.txt"
# with open(filename) as file:
#     talabalar = file.readlines()
    
# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)

# filename = "data/ustozlar.txt"
# with open(filename, "w") as file:
#     file.write("anvar narzullaev")

# filename = "data/new_file.txt"
# ism = "Olimjon Hasanov"
# tyil = 2004
# with open(filename, "w") as file:
#     file.write(ism + "\n")
#     file.write(str(tyil) + "\n")

# with open(filename, "a") as file:
#     file.write("Alijon Valiyev\n")
#     file.write("2000")

# talaba1 = {"ism":"hasan", "familiya":"husanov", "tyil":2003, "kurs":2}
# talaba2 = {"ism":"alijon", "familiya": "valiyev", "tyil":2004, "kurs":1}

# with open("data/info", "wb") as file:
#     pickle.dump(talaba1, file)
#     pickle.dump(talaba2, file)

# with open("data/info", "rb") as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)

# print(talaba1)
# print(talaba2)