print ("GYM Memiliki 3 Kategori Keanggotaan:")
print("1.Reguler (Fasilitas GYM biasa)")
print("2.Premium (Fasilitas GYM & Sauna)")
print("3.VIP (Fasilitas GYM, Sauna & Kolam Renang)")
anggotaBian = int(input("Pilih anggota gym 1-3:"))
usiaBian = int(input("Berapa usiamu?"))
if anggotaBian == 1:
    print("kamu member Reguler mendapatkan fasilitas GYM Biasa")
elif anggotaBian == 2:
    print("Kamu member Premium mendapatkan fasilitas GYM dan Sauna")
    if usiaBian > 50:
        print("kamu mendapatkan diskon sebesar 10%")
    else:
        print("Karena usiamu tidak diatas 50 tidak dapat diskon")
elif anggotaBian == 3:
    print("Kamu member VIP mendapatkan fasilitas GYM, Sauna & Kolam Renang")
    if usiaBian > 50:
        print("kamu mendapatkan diskon sebesar 10%")
    else:
        print("Karena usiamu tidak diatas 50 tidak dapat diskon")
else:
    print("Masukan rentang 1-3")
