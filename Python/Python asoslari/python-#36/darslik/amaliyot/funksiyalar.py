def kattasi(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    

def katta_harf(royhat):
    return [element.title() for element in royhat]

def juft_son(royhat):
    juft = []
    for element in royhat:
        if element % 2 == 0:
            juft.append(element)
    return juft