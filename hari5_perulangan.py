# Hari 5: Perulangan (for & while)

# Perulangan dengan for
print("Cetak angka 1 sampai 5:")
for i in range(1, 6):
    print(i)

# Perulangan dengan while
print("\nCetak angka 1 sampai 5 dengan while:")
x = 1
while x <= 5:
    print(x)
    x += 1

# Gunakan break dan continue
print("\nPerulangan dengan break:")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("\nPerulangan dengan continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Studi Kasus: Cetak segitiga bintang
print("\nSegitiga Bintang:")
baris = int(input("Masukkan jumlah baris: "))
for i in range(1, baris + 1):
    print("*" * i)
