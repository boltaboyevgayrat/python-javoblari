import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread_1_task():
    with lock_a:
        print("Thread 1: Lock A ni oldi")
        time.sleep(1)  # Thread 2 ga Lock B ni olish uchun vaqt berish
        print("Thread 1: Lock B ni kutmoqda...")
        with lock_b:
            print("Thread 1: Lock B ni ham oldi")

def thread_2_task():
    with lock_b:
        print("Thread 2: Lock B ni oldi")
        time.sleep(1)  # Thread 1 ga Lock A ni olish uchun vaqt berish
        print("Thread 2: Lock A ni kutmoqda...")
        with lock_a:
            print("Thread 2: Lock A ni ham oldi")

# Ishga tushirish
t1 = threading.Thread(target=thread_1_task)
t2 = threading.Thread(target=thread_2_task)

t1.start()
t2.start()




lock_a = threading.Lock()
lock_b = threading.Lock()

def safe_thread_task(name, first_lock, second_lock):
    print(f"{name}: Ish boshladi")
    # Tartib qat'iy: doimo birinchi ko'rsatilgan lock, keyin ikkinchisi
    with first_lock:
        print(f"{name}: Birinchi lockni oldi")
        time.sleep(1)
        print(f"{name}: Ikkinchi lockni kutmoqda...")
        with second_lock:
            print(f"{name}: Ikkala lockni ham oldi va ishni bitirdi")

# Ikkala oqim ham LOCK_A ni birinchi, keyin LOCK_B ni so'raydi
t1 = threading.Thread(target=safe_thread_task, args=("Thread 1", lock_a, lock_b))
t2 = threading.Thread(target=safe_thread_task, args=("Thread 2", lock_a, lock_b))

t1.start()
t2.start()

t1.join()
t2.join()
print("Dastur muvaffaqiyatli yakunlandi!")
