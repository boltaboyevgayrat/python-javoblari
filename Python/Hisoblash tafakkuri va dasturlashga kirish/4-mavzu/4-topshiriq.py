# 4. Satrdagi unli harflar sonini sanaydigan count_vowels (text) funksiyani ishlab 
# chiqing.

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
            
    return count

print(count_vowels('salom'))