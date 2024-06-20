
# Shaxmat taxtasining quyi chap burchagini koordinata boshi deb hisoblab, (uning kataklari 1 dan 8 gacha  butun sonlar bilan belgilangan), uning ikkala qismidan bittadan katakcha  berilgan. Tanlangan katakchalar bir xil rangdaligi rostlikka tekshirilsin


x1 = int(input("Birinchi katakchaning x koordinatasini kiriting: "))
y1 = int(input("Birinchi katakchaning y koordinatasini kiriting: "))
x2 = int(input("Ikkinchi katakchaning x koordinatasini kiriting: "))
y2 = int(input("Ikkinchi katakchaning y koordinatasini kiriting: "))

# Birinchi katakchaning rangini tekshirish
first_cell_color = (x1 + y1) % 2
# Ikkinchi katakchaning rangini tekshirish
second_cell_color = (x2 + y2) % 2

# Ikkala katakchaning rangi bir xil ekanligini tekshirish
if first_cell_color == second_cell_color:
    print(True)
else:
    print(False)
