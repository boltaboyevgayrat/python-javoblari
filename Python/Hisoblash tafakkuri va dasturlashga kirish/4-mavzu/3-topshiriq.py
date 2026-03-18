# 3. Ko‘rsatilgan belgidan berilgan o‘lchamdagi to‘g‘ri to‘rtburchakni ekranga 
# chiqaruvchi draw_rectangle (width, height, symbol) protsedurasini yarating

def draw_rectangle(width, height, symbol):
    for i in range(height):
        print(symbol * width)

draw_rectangle(5, 3, '#')