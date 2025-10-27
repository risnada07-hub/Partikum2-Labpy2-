import random

n = int(input("Masukkan jumlah n: "))
i = 0

while i < n:
    angka = random.random()
    if angka < 0.5:
        print(angka)
        i += 1