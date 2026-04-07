import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time

# 1. Bitta sahifani yuklab olish va qayta ishlash funksiyasi
async def fetch_and_parse(session, url):
    try:
        print(f"Yuklanmoqda: {url}")
        async with session.get(url, timeout=10) as response:
            # Sahifa matnini asinxron o'qish
            html = await response.text()
            
            # BeautifulSoup yordamida qayta ishlash (parsing)
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string if soup.title else "Sarlavha topilmadi"
            
            print(f"Tugallandi: {url} -> [{title.strip()}]")
            return title.strip()
    except Exception as e:
        print(f"Xatolik ({url}): {e}")
        return None

# 2. Asosiy asinxron boshqaruvchi
async def main():
    urls = [
        "https://www.google.com",
        "https://www.wikipedia.org",
        "https://www.python.org",
        "https://www.github.com",
        "https://stackoverflow.com"
    ]

    # Bitta sessiya orqali barcha so'rovlarni yuborish (resursni tejaydi)
    async with aiohttp.ClientSession() as session:
        # Barcha vazifalarni (tasks) yaratish
        tasks = [fetch_and_parse(session, url) for url in urls]
        
        # Vazifalarni parallel ravishda ishga tushirish va natijalarni kutish
        results = await asyncio.gather(*tasks)
        
    print(f"\nJami {len([r for r in results if r])} ta sahifa muvaffaqiyatli skreping qilindi.")

if __name__ == "__main__":
    start_time = time.time()
    
    # Event loop ni ishga tushirish
    asyncio.run(main())
    
    print(f"Umumiy sarflangan vaqt: {time.time() - start_time:.2f} soniya")