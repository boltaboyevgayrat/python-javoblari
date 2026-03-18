# 5. Dastlabki n ta Fibonachchi sonlari ro‘yxatini qaytaruvchi generate_fibonacci (n) 
# funksiyasini yozing.

def generate_fibonacci(n):
    fib = []
    
    a, b = 0, 1
    for i in range(n):
        fib.append(a)
        a, b = b, a + b
        
    return fib

print(generate_fibonacci(7))