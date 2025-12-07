# Input Bilangan
bil = int(input("Masukan Bilangan: "))

# Logika
if bil == 0:
    print("0 Bukan Bilangan Ganjil atau Genap")
elif bil % 2 == 0:
    print(bil, "Adalah Bilangan Genap")
else:
    print(bil, "Adalah Bilangan Ganjil")