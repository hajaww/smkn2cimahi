while True:
    print("\n=== Main Menu ===")
    print("1. Hitung Tanggal Lahir \n2. Keluar")
    bianPilihan = int(input("Pilih (1/2): "))
    if bianPilihan == 1:
        bianTanggal = int(input("Masukan Tanggal: "))
        bianBulan = int(input("Masukan Bulan(Angka): "))
        bianTahun = int(input("Masukan Tahun: "))
        if bianBulan <= 12:
            bianHitungBulan = 12 - bianBulan + 1
            if bianBulan == 3 and bianTanggal >= 21 or bianBulan == 4 and bianTanggal <= 19:
                bianZodiak = "Aries"
            elif bianBulan == 4 and bianTanggal >= 20 or bianBulan == 5 and bianTanggal <= 20:
                bianZodiak = "Taurus"
            elif bianBulan == 5 and bianTanggal >= 21 or bianBulan == 6 and bianTanggal <= 20:
                bianZodiak = "Gemini"
            elif bianBulan == 6 and bianTanggal >= 21 or bianBulan == 7 and bianTanggal <= 22:
                bianZodiak = "Cancer"
            elif bianBulan == 7 and bianTanggal >= 23 or bianBulan == 8 and bianTanggal <= 22:
                bianZodiak = "Leo"
            elif bianBulan == 8 and bianTanggal >= 23 or bianBulan == 9 and bianTanggal <= 22:
                bianZodiak = "Virgo"
            elif bianBulan == 9 and bianTanggal >= 23 or bianBulan == 10 and bianTanggal <= 21:
                bianZodiak = "Libra"
            elif bianBulan == 10 and bianTanggal >= 23 or bianBulan == 11 and bianTanggal <= 21:
                bianZodiak = "Scorpio"
            elif bianBulan == 11 and bianTanggal >= 22 or bianBulan == 12 and bianTanggal <= 21:
                bianZodiak = "Sagittarius"
            elif bianBulan == 12 and bianTanggal >= 22 or bianBulan == 1 and bianTanggal <= 19:
                bianZodiak = "Capricorn"
            elif bianBulan == 1 and bianTanggal >= 20 or bianBulan == 2 and bianTanggal <= 18:
                bianZodiak = "Aquarius"
            elif bianBulan == 2 and bianTanggal >= 19 or bianBulan == 3 and bianTanggal <= 20:
                bianZodiak = "Pisces"
        else:
            print("Bulan tidak bisa lebih dari 12")
        if bianTahun <= 2025:
            bianUmur = 2025 - bianTahun - 1
        else:
            print("Tahun tidak bisa lebih dari 2024")
    elif bianPilihan == 2:
        print("Kamu Keluar Program")
        break
    else:
        print("Inputan Tidak Valid Pilih (1/2)")

    print("\nTanggal Lahir:",bianTanggal,"\nBulan Lahir:",bianBulan, "\nZodiak:", bianZodiak, "\nTahun:", bianTahun, "\nUmurmu:",bianUmur, "Umur")