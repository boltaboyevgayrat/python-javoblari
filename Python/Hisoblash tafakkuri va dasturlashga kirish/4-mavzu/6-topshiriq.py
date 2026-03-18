# 6.Raqamlar ro'yxatini qabul qiladigan va ularning arifmetik o'rtacha qiymatini 
# qaytaradigan calculate_average(number_list) funktsiyasini yarating.

def calculate_average(number_list):
    total = sum(number_list)
    count = len(number_list)
    average = total / count
    return average

print(calculate_average([2, 4, 6, 8]))