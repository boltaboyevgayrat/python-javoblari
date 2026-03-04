def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Test
num = int(input("Son kiriting: "))
if is_prime(num):
    print("Tub son")
else:
    print("Tub emas")
