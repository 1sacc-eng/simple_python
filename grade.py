# === Biodata ===
nama = input("Nama: ")
npm = int(input("Npm: "))
kelas = input("Kelas: ")

# === Nilai Total ===
matkul = input("Mata Kuliah: ")
uts = int(input("Nilai UTS:"))
uas = int(input("Nilai UAS: "))
total = int((0.5*uts) + (0.5*uas))

# === Grade Nilai ===
if 86 <= total <= 100:
    grade = "A"
elif 71 <= total <= 85:
    grade = "B"
elif 61 <= total <= 70:
    grade = "C"
else:
    grade = "D"

# === Output ===
print("\n" "===== HASIL PENILAIAN MAHASISWA =====")
print("Nama         :",nama)
print("NPM          :",npm)
print("Kelas        :",kelas)
print("-"*40)
print("Mata Kuliah  :",matkul)
print("Nilai UTS    :",uts)
print("Nilai UAS    :",uas)
print("Total Nilai  :",total)
print("Grade        :",grade)
print("-"*40)