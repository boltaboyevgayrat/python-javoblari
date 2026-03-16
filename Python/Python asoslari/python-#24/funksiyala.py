from uzwords import words
import random as r

def get_words():
    return words[r.randint(0, 19000)]
print(get_words())

def soz_top():
    soz = get_words()
    print(soz)
    qism_soz = ''
    for i in range(len(soz)):
        qism_soz += '-'
    print(f'{len(soz)} ta harfdan iborat so\'z o\'yladim. Topa olasizmi?')
    print(qism_soz)
    harflar = ''
    qadam = 0
    while True:
        index = -1
        qadam += 1
        harf = input('Харф киритинг: ')
        if harf not in harflar:
            harflar += harf
            if harf in soz:
                print(f'{harf} harfi to\'g\'ri.')
                for j in soz:
                    index += 1
                    if harf == j:
                        qism_soz = qism_soz[:index] + harf + qism_soz[index+1:]
            else:
                print('Bunday harf yoq.')
        else:
            print('Bu harfni kiritgansiz.Boshqa harf kiriting.')

        if qism_soz != soz:       
            print(qism_soz)
            print(f'Shu vaqtgacha kiritgan harflaringiz: {harflar}')
        else:
            print(f'Tabriklayman! {soz} so\'zini {qadam} ta urinishda topdingiz.')
            break
    return qadam

soz_top()