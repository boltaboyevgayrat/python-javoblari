# Fayldagi so'zlar sonini hisoblash va eng ko'p takrorlangan so'zni aniqlash

def count_words_and_find_most_common(file_path):
    try:
        # Faylni ochish va o'qish
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Matnni so'zlarga ajratish
        words = text.split()
        
        # So'zlar sonini hisoblash
        total_words = len(words)
        print(f"Faylda jami {total_words} ta so'z bor.")
        
        # So'zlarni lug'atda sanash
        word_count = {}
        for word in words:
            word = word.lower().strip(",.?!;:\"'")  # Kichik harfga o'tkazish va tinish belgilarini olib tashlash
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        # Eng ko'p takrorlangan so'zni aniqlash
        most_common_word = max(word_count, key=word_count.get)
        print(f"Eng ko'p takrorlangan so'z: '{most_common_word}' ({word_count[most_common_word]} marta)")
    
    except FileNotFoundError:
        print("Fayl topilmadi. Iltimos, fayl yo'lini tekshiring.")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

