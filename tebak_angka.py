import random

angka_rahasia = random.randint(1, 20)
ronde = 0
max_ronde = 5

print("=== TEBAK ANGKA RAHASIA ===")
print("Naya sedang memikirkan sebuah angka.")
print("Anda memiliki", max_ronde, "kesempatan untuk menebak angka itu.")

while ronde < max_ronde:
    tebakan = int(input("\nTebakan anda: "))
    ronde += 1

    if tebakan < angka_rahasia:
        print("Angka nya terlalu kecil, coba lagi")
    elif tebakan > angka_rahasia:
        print("Angkanya terlalu besar, coba lagi")
    else:
        print("SELAMAT TEBAKAN ANDA BENAR!")
        print("Naya sedang memikirkan angka ", angka_rahasia)
        exit(0)
    print("Kesempatan anda terisa ", max_ronde - ronde)

print("\nKesempatan anda habis...")
print("Angka yang sedang dipikirkan Naya adalah ", angka_rahasia)