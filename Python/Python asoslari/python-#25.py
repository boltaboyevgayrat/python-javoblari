import random as r

def son_top(x):
    son = r.randint(0, x)
    qadam = 0
    while True:
        tahmin = int(input('Sonni tahmin qiling: '))
        qadam += 1
        if son > tahmin:
            print('Men o\'ylagan son kattaroq.Qaytadan tahmin qiling.')
            continue
        elif son < tahmin:
            print('Men o\'ylagan son kichikroq.Qaytadan tahmin qiling.')
            continue
        else:
            print(f'To\'g\'ri. {qadam}-urunishda topdingiz.')
            break
    return qadam

def son_top_pc(x):
    qadam = 0
    min = 0
    while True:
        tahmin = r.randint(min, x)
        qadam += 1
        print(f'Mening tahminim {tahmin}.')
        tek = input('Agar tahminim to\'g\'ti bo\'lsa "to\'gri" deb yozing.Agar kattaroq son o\'ylagan bo\'lsangiz "+", aks holda "-" yozing.')
        if tek == 'to\'g\'ri':
            print(f'Men {qadam} ta tahminda topdim.')
            break
        elif tek == '+':
            min = tahmin + 1
            continue
        else:
            x = tahmin - 1
            continue
    return qadam
        

print('Son top o\'yiniga xush kelibsiz!')
x = int(input('Qaysi oraliqdagi sonlarda o\'ynaymiz? >> '))

print('Unday bo\'lsa men son o\'yladim')

qadam1 = son_top(x)

input('Endi siz son \'ylang va ixtiyoriy tugmani bosing.Men topaman. >>')

qadam2 = son_top_pc(x)
if qadam1<qadam2:
    print('Siz g\'olib bo\'ldingiz.')
elif qadam2<qadam1:
    print('Men g\'olib bo\'dim.')
else:
    print('O\'yi durrang bo\'ldi.')
print("O'yin tugadi.")


