# Hari 7: Fungsi & Parameter

# Fungsi sederhana
def sapa():
    print("Halo, selamat datang!")

sapa()

# Fungsi dengan parameter
def sapa_nama(nama):
    print("Halo,", nama)

sapa_nama("Atma")
sapa_nama("Budi")

# Fungsi dengan return
def tambah(a, b):
    return a + b

hasil = tambah(3, 4)
print("Hasil penjumlahan:", hasil)

# Studi kasus: hitung luas segitiga
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

a = float(input("Masukkan alas: "))
t = float(input("Masukkan tinggi: "))
print("Luas segitiga:", luas_segitiga(a, t))
