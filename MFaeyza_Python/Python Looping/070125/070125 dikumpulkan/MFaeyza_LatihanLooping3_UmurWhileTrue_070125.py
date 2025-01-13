bianLahir = int(input("Masukan Tahun Lahir Fara: "))
while True:
    bianTahun = int(input("Masukan Tahun Saat ini: "))
    if bianTahun > bianLahir:
        bianUmur = bianTahun - bianLahir
        print("Umur Fara adalah",bianUmur,"Tahun")
        break
    else:
        print("Tahun saat ini tidak boleh lebih kecil dari tahun lahir")




