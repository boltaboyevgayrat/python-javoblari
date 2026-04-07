import multiprocessing
import time
import random

# Standart Merge Sort (Ketma-ket variant)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Parallel Merge Sort
def parallel_merge_sort(arr, proc_count):
    if proc_count <= 1 or len(arr) <= 1000:  # Kichik qismlarni oddiy saralaymiz
        return merge_sort(arr)

    mid = len(arr) // 2
    # Pipe orqali natijalarni qaytarib olamiz
    parent_conn, child_conn = multiprocessing.Pipe()
    
    # Chap yarimni yangi jarayonda ishga tushiramiz
    p = multiprocessing.Process(target=worker, args=(arr[:mid], child_conn, proc_count // 2))
    p.start()
    
    # O'ng yarimni joriy jarayonda saralaymiz
    right = parallel_merge_sort(arr[mid:], proc_count - proc_count // 2)
    
    # Chap yarim natijasini kutamiz
    left = parent_conn.recv()
    p.join()
    
    return merge(left, right)

def worker(arr, conn, proc_count):
    res = parallel_merge_sort(arr, proc_count)
    conn.send(res)
    conn.close()

def benchmark():
    sizes = [10000, 100000, 500000]
    cores = multiprocessing.cpu_count()
    
    print(f"{'Massiv hajmi':<15} | {'Oddiy (sek)':<12} | {'Parallel (sek)':<12} | {'Tezlanish'}")
    print("-" * 60)
    
    for size in sizes:
        data = [random.randint(0, size) for _ in range(size)]
        
        # Ketma-ket variant
        start = time.time()
        merge_sort(data)
        seq_time = time.time() - start
        
        # Parallel variant
        start = time.time()
        parallel_merge_sort(data, cores)
        par_time = time.time() - start
        
        speedup = seq_time / par_time
        print(f"{size:<15} | {seq_time:<12.4f} | {par_time:<12.4f} | {speedup:.2f}x")

if __name__ == "__main__":
    benchmark()