def add_poly(A, B):
    n = max(len(A), len(B))
    res = [0] * n
    for i in range(len(A)): res[i] += A[i]
    for i in range(len(B)): res[i] += B[i]
    return res

def sub_poly(A, B):
    n = max(len(A), len(B))
    res = [0] * n
    for i in range(len(A)): res[i] += A[i]
    for i in range(len(B)): res[i] -= B[i]
    return res

def multiply_poly(A, B):
    n = len(A)
    
    # Bazaviy holat: agar ko'phad darajasi 1 bo'lsa
    if n == 1:
        return [A[0] * B[0]]

    mid = n // 2

    # Bo'lish
    A_low = A[:mid]
    A_high = A[mid:]
    B_low = B[:mid]
    B_high = B[mid:]

    # Rekursiv ko'paytirish (3 ta asosiy ko'paytma)
    P1 = multiply_poly(A_high, B_high) # High * High
    P2 = multiply_poly(A_low, B_low)   # Low * Low
    
    A_sum = add_poly(A_low, A_high)
    B_sum = add_poly(B_low, B_high)
    P3 = multiply_poly(A_sum, B_sum)   # (Low+High) * (Low+High)

    # O'rta hadni hisoblash: P3 - P1 - P2
    middle_term = sub_poly(sub_poly(P3, P1), P2)

    # Natijani yig'ish (darajalarni hisobga olgan holda)
    result = [0] * (2 * n - 1)
    
    for i in range(len(P2)):
        result[i] += P2[i]
    for i in range(len(middle_term)):
        result[i + mid] += middle_term[i]
    for i in range(len(P1)):
        result[i + 2 * mid] += P1[i]

    return result

# Sinov: (1 + 2x) * (3 + 4x)
# Kutilayotgan natija: 3 + 10x + 8x^2 -> [3, 10, 8]
poly1 = [1, 2]
poly2 = [3, 4]
print(f"Natija: {multiply_poly(poly1, poly2)}")