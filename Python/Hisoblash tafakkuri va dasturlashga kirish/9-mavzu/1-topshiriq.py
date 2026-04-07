import math
import time
import multiprocessing

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def sequential_prime_search(limit):
    start_time = time.time()
    primes = [n for n in range(limit) if is_prime(n)]
    end_time = time.time()
    return len(primes), end_time - start_time

def parallel_prime_search(limit):
    start_time = time.time()
    
    # Protsessor yadrolari sonini aniqlash
    num_cores = multiprocessing.cpu_count()
    
    with multiprocessing.Pool(processes=num_cores) as pool:
        # map funksiyasi is_prime ni range(limit) dagi har bir songa qo'llaydi
        results = pool.map(is_prime, range(limit))
    
    # Faqat True bo'lgan (tub) sonlarni ajratib olish
    primes = [n for n, prime in enumerate(results) if prime]
    
    end_time = time.time()
    return len(primes), end_time - start_time

if __name__ == "__main__":
    limit = 1_000_000  # 1 milliongacha bo'lgan sonlar
    
    print(f"Qidiruv oralig'i: 0 dan {limit} gacha\n")
    
    # Ketma-ket variant
    print("Ketma-ket qidiruv boshlandi...")
    seq_count, seq_time = sequential_prime_search(limit)
    print(f"Topildi: {seq_count} ta tub son. Vaqt: {seq_time:.2f} soniya.\n")
    
    # Parallel variant
    print(f"Parallel qidiruv ({multiprocessing.cpu_count()} yadroda) boshlandi...")
    par_count, par_time = parallel_prime_search(limit)
    print(f"Topildi: {par_count} ta tub son. Vaqt: {par_time:.2f} soniya.\n")
    
    # Xulosa
    speedup = seq_time / par_time
    print(f"Tezlanish koeffitsiyenti: {speedup:.2f} barobar.")
