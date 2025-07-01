# Hari 4: Percabangan if, elif, else

# Percabangan sederhana
nilai = int(input("Masukkan nilai ujian: "))

if nilai >= 90:
    print("Nilai kamu A")
elif nilai >= 80:
    print("Nilai kamu B")
elif nilai >= 70:
    print("Nilai kamu C")
elif nilai >= 60:
    print("Nilai kamu D")
else:
    print("Nilai kamu E (remedial)")

# Studi kasus: login sederhana
username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == "admin" and password == "1234":
    print("Login berhasil!")
else:
    print("Username atau password salah.")
