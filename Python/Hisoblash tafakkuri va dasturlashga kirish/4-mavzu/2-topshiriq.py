# 2. n sonning faktorialini hisoblaydigan calculate_factorial (n) funksiyani ishlab 
# chiqing (n! = 1 × 2 × 3 ×... × n).

def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

n = int(input('Birorta butun son kiriting: '))

print(calculate_factorial(n))