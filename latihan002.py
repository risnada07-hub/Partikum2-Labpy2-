print("Program Mengurutkan Data")

data = []
n = int(input("Masukkan jumlah data: "))

for i in range(n):
    bil = int(input(f"Bilangan ke-{i+1}: "))
    data.append(bil)

data.sort()
print("Urutan bilangan:", *data)