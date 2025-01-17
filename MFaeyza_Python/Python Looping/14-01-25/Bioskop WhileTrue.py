while True:

    print("\n==== Menu Aplikasi Tiket Bioskop ==== \n1.Hitung Harga Tiket\n2.Keluar")
    bianMenu = (input("Pilih Menu (1/2): "))
    if (bianMenu.replace('.', '', 1).isdigit()):
        bianMenu = float(bianMenu)
    if bianMenu == 1:
        print("\nPilih Jenis Theatre: \n1. Reguler (Rp50.000)\n2. Premier (Rp80.000)\n3. VIP (Rp120.000)")
        bianTheatre = (input("Pilih Jenis Theatre (1/2/3): "))
        if (bianTheatre.replace('.', '', 1).isdigit()):
            bianTheatre = float(bianTheatre)

        if bianTheatre == 1:
            print("\nKamu memilih Theatre Reguler dengan harga Rp50.000")
            bianTiket = (input("Masukan Jumlah Tiket: "))
            bianHarga = 50000
            if (bianTiket.replace('.','',1).isdigit()):
                bianTiket = float(bianTiket)
                bianTotal = bianTiket * bianHarga
                print(f"Total Tiket: {bianTiket} Total Harga : Rp{bianTotal}")
                if bianTiket > 3:
                    print("karena pembelian tiket lebih dari 3 kamu mendapatkan diskon sebesar 10%")
                    bianDiskon = bianTotal * 0.1
                    bianDiskonTotal = bianTotal - bianDiskon
                    print("Harga Setelah Diskon:", bianDiskonTotal)
            else:
                print("Maaf, inputan tidak valid")


        elif bianTheatre == 2:
            print("\nKamu memilih Theatre Premier dengan harga Rp80.000")
            bianTiket = (input("Masukan Jumlah Tiket: "))
            bianHarga = 80000
            if (bianTiket.replace('.','',1).isdigit()):
                bianTiket = float(bianTiket)
                bianTotal = bianTiket * bianHarga
                print(f"Total Tiket: {bianTiket} Total Harga : Rp{bianTotal}")
                if bianTiket > 3:
                    print("karena pembelian tiket lebih dari 3 kamu mendapatkan diskon sebesar 10%")
                    bianDiskon = bianTotal * 0.1
                    bianDiskonTotal = bianTotal - bianDiskon
                    print("Harga Setelah Diskon:", bianDiskonTotal)
            else:
                print("Maaf, inputan tidak valid")


        elif bianTheatre == 3:
            print("\nKamu memilih Theatre VIP dengan harga Rp120.000")
            bianTiket = (input("Masukan Jumlah Tiket: "))
            bianHarga = 120000

            if (bianTiket.replace('.','', 1).isdigit()):
                    bianTiket = float(bianTiket)
                    bianTotal = bianTiket * bianHarga
                    print(f"Total Tiket: {bianTiket} tiket Total Harga : Rp{bianTotal}")
                    if bianTiket > 3:
                        print("karena pembelian tiket lebih dari 3 kamu mendapatkan diskon sebesar 10%")
                        bianDiskon = bianTotal * 0.1
                        bianDiskonTotal = bianTotal - bianDiskon
                        print("Harga Setelah Diskon:", bianDiskonTotal)
            else:
                print("Maaf, inputan tidak valid")

        else:
            print("Maaf, inputan tidak valid")
    elif bianMenu == 2:
        print("Terimakasih sudah menggunakan Program Kami")
    else:
        print("Masukan Inputan Yang Sesuai")