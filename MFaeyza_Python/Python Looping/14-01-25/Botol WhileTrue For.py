while True:
    print("=== Main Menu === \n1. Hitung Botol \n2. Keluar Program")
    bianJumlah = 0
    bianPilihan = int(input("Pilih (1/2): "))
    if bianPilihan == 1:
       bianBotol = int(input("Masukan Botol dihari pertama: "))
       bianProduksi = int(input("Masukan Target Produksi Botol PerHari: "))
       bianHari = 1
       for bianTotal in range(0,10):
            print("Hari ke:", bianHari, "Jumlah Produksi:", bianBotol)
            bianBotol += bianProduksi
            bianJumlah += bianBotol - bianProduksi
            bianHari += 1
    elif bianPilihan == 2:
        print("Terimakasih sudah menggunaka program kami")
        break
    else:
        print("Masukan Inputan Yang Valid")
    print("Jadi Total Produksi selama 10 hari sebanyak:",bianJumlah)