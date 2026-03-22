try:
    a = input(' a ni kiriting: ')
    b = input(' b ni kiriting: ')
    a = int(a)
    b = int(b)
    print('a/b=', a/b)
except ValueError:
    print('Faqat butun son kiritish kerak!')
except ZeroDivisionError:
    print("o ga bo'lish mumkin emas!")
    