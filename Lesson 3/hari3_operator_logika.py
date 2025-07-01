# Hari 3: Operator & Logika

# Operator Aritmatika
a = 10
b = 3

print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)
print("Modulus (sisa bagi):", a % b)
print("Pangkat:", a ** b)
print("Pembagian bulat:", a // b)

# Operator Perbandingan
print("Apakah a > b?", a > b)
print("Apakah a == 10?", a == 10)
print("Apakah a != b?", a != b)

# Operator Logika
x = True
y = False

print("AND:", x and y)
print("OR:", x or y)
print("NOT x:", not x)

# Contoh Kasus: Cek usia
umur = int(input("Masukkan umur kamu: "))
if umur >= 17 and umur <= 60:
    print("Kamu boleh membuat SIM.")
else:
    print("Kamu belum/tidak boleh membuat SIM.")
