while True:
    print("=== Main Menu ===")
    print("1. Hitung Tanggal Lahir \n2. Keluar")
    bianPilihan = int(input("Pilih (1/2)"))
    if bianPilihan == 1:
        bianTanggal = int(input("Masukan Tanggal: "))
        bianBulan = int(input("Masukan Bulan(Angka): "))
        bianTahun = int(input("Masukan Tahun: "))
        if bianBulan <= 12:
            bianHitungBulan = 12 - bianBulan + 1
        else:
            print("Bulan tidak bisa lebih dari 12")
        if bianTahun <= 2025:
            bianHitungTahun = 2025 - bianTahun - 1
        else:
            print("Tahun tidak bisa lebih dari 2024")
        print(f" {bianHitungTahun} Tahun \n {bianHitungBulan} Bulan")
    elif bianPilihan == 2:
        print("Kamu Keluar Program")
        break
    else:
        print("Inputan Tidak Valid Pilih (1/2)")
