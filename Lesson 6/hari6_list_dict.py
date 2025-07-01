# Hari 6: Struktur Data - List & Dictionary

# List
buah = ["apel", "jeruk", "pisang"]
print("List buah:", buah)
print("Buah pertama:", buah[0])

buah.append("mangga")
buah.remove("jeruk")
print("List setelah diubah:", buah)

# Looping list
for item in buah:
    print("Saya suka", item)

# Dictionary
siswa = {
    "nama": "Atma",
    "umur": 17,
    "kelas": "XII RPL"
}
print("\nData siswa:", siswa)
print("Nama:", siswa["nama"])

# Tambah dan ubah data
siswa["umur"] = 18
siswa["jurusan"] = "Rekayasa Perangkat Lunak"

# Looping dictionary
for key, value in siswa.items():
    print(key + ":", value)
