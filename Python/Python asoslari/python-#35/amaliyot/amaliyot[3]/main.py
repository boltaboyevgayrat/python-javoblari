mevalar = ['olma', 'banan', 'uzum']

try:
    indeks = int(input('Indeksni kiriting: '))
    print(mevalar[indeks])
except ValueError:
    print('Faqat butun son kiriting!')
except IndexError:
    print('Bunaqa indeksli meva yo\'q')
