#Data Diri
#nama = input("Nama: ")
umur = int(input("Umur: "))
tinggi = float(input("Tinggi: "))
berat_badan = int(input("Berat Badan: "))
print()

print("=== Data Diri ===")
print("Nama saya:", nama,)
print("Umur saya: ",umur, "tahun")
print("Tinggi Badan Saya: ", tinggi, "cm")
print("Berat Badan Saya: ", berat_badan, "kg")
print()

print("=== CONTOH OPERATOR ===")

#1. Operator Aritmatika
berat_ideal = int(tinggi - 100)
print("1. Berat Badan Ideal: ", berat_ideal)

#2. Operator Perbandingan
if umur >= 17:
    print("2. Boleh Membuat KTP")
else:
    print("2. Belom Boleh Membuat KTP")

#3. Operator Logika
logika = umur > 17
print("3. Apakah umur lebih besar dari 15? ->", logika)

#4. Operator Penugasan
umur -= 2
print("4. Umur Saya 2 Tahun Lalu Adalah: ", umur)