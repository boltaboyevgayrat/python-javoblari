import multiprocessing
import numpy as np
import time

# Har bir qatorni hisoblash uchun ishchi funksiya
def multiply_row(args):
    row_idx, matrix_a, matrix_b = args
    # Natijaviy matritsaning bitta qatorini hisoblash
    return np.dot(matrix_a[row_idx], matrix_b)

def parallel_matrix_multiply(A, B, num_processes):
    # Natijaviy matritsa o'lchamini aniqlash
    rows_a = A.shape[0]
    
    # Ishchi jarayonlar uchun argumentlar ro'yxatini tayyorlash
    tasks = [(i, A, B) for i in range(rows_a)]
    
    # Jarayonlar pulini yaratish
    with multiprocessing.Pool(processes=num_processes) as pool:
        # Vazifalarni parallel bajarish
        result_rows = pool.map(multiply_row, tasks)
        
    return np.array(result_rows)

if __name__ == "__main__":
    # 1. Katta matritsalar yaratish (masalan, 500x500)
    size = 500
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    
    cores = multiprocessing.cpu_count()
    print(f"Matritsa o'lchami: {size}x{size}")
    print(f"Yadrolar soni: {cores}")

    # 2. Ketma-ket (Sequential) ko'paytirish
    start = time.time()
    result_seq = np.dot(A, B)
    seq_time = time.time() - start
    print(f"Ketma-ket ko'paytirish vaqti: {seq_time:.4f} soniya")

    # 3. Parallel ko'paytirish
    start = time.time()
    result_par = parallel_matrix_multiply(A, B, cores)
    par_time = time.time() - start
    print(f"Parallel ko'paytirish vaqti: {par_time:.4f} soniya")

    # 4. Natijalarni tekshirish
    print(f"Tezlanish: {seq_time / par_time:.2f}x")