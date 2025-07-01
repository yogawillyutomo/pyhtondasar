# Hari 2: Variabel & Tipe Data

# Tipe data dasar
nama = "Atma"           # str
umur = 17               # int
tinggi = 165.5          # float
is_student = True       # bool

# Cek tipe data
print(type(nama))
print(type(umur))
print(type(tinggi))
print(type(is_student))

# Konversi tipe data
angka = "42"
angka_int = int(angka)
print("Angka setelah konversi:", angka_int)

# Input dengan konversi
umur_input = int(input("Masukkan umur kamu: "))
print("Umur kamu 5 tahun lagi adalah:", umur_input + 5)
