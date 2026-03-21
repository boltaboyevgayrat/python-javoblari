# functions.py

def daily_planner():
    with open("data/rejalar.txt", "a", encoding="utf-8") as file:
        while True:
            plan = input("Bugungi rejangiz nima? (To'xtatish uchun 'stop' deb yozing): ")
            if plan.lower() == "stop":
                print("Dastur to'xtatildi.")
                break
            file.write(plan + "\n")
            print("Reja saqlandi.")

