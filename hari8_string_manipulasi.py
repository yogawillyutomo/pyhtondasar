# Hari 8: Manipulasi String

# String dasar
teks = "Halo, Dunia!"
print(teks.lower())
print(teks.upper())
print(teks.replace("Dunia", "Python"))
print(teks.split(","))
print(teks.strip("!"))

# Gabung string
nama = "Atma"
umur = 17
kalimat = f"Nama saya {nama}, umur saya {umur} tahun"
print(kalimat)

# Cek karakter dalam string
print("Halo" in teks)
print("Python" not in teks)
