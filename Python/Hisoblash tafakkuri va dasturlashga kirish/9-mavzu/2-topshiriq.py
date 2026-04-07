import threading
import queue
import urllib.request
import os
import time

# 1. Yuklab olish funksiyasi (Ishchi oqim uchun)
def file_downloader(q, thread_id):
    while True:
        try:
            # Navbatdan bitta URLni bloklanmagan holda olamiz
            url = q.get(timeout=3) 
            file_name = url.split("/")[-1]
            print(f"Oqim-{thread_id}: {file_name} yuklanmoqda...")
            
            # Faylni saqlash
            urllib.request.urlretrieve(url, file_name)
            
            print(f"Oqim-{thread_id}: {file_name} muvaffaqiyatli yuklandi.")
            
            # Vazifa bajarilgani haqida navbatga xabar berish
            q.task_done()
        except queue.Empty:
            # Navbat bo'sh bo'lsa, oqim ishini to'xtatadi
            break
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")
            q.task_done()

# 2. Asosiy boshqaruv qismi
def main():
    # Yuklanishi kerak bo'lgan fayllar ro'yxati (misol uchun)
    urls = [
        "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
        "https://python.org/static/img/python-logo.png",
        "https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png",
        "https://www.github.com/fluidicon.png"
    ]

    # Oqim xavfsiz navbat yaratish
    download_queue = queue.Queue()

    # URLlarni navbatga qo'shish
    for url in urls:
        download_queue.put(url)

    # Oqimlar (Thread) sonini belgilash
    num_threads = 3
    threads = []

    start_time = time.time()

    # Ishchi oqimlarni yaratish va ishga tushirish
    for i in range(num_threads):
        t = threading.Thread(target=file_downloader, args=(download_queue, i))
        t.start()
        threads.append(t)

    # Barcha oqimlar tugashini kutish
    for t in threads:
        t.join()

    end_time = time.time()
    print(f"\nBarcha fayllar {end_time - start_time:.2f} soniyada yuklab olindi.")

if __name__ == "__main__":
    main()
