while True:
    print("\n=== Menu Calculator ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")
    BianPilih = int(input("Pilih Menu (1/2/3/4/5): "))
    if BianPilih == 1:
        print("Anda Memilih Tambah")
        bianAngka1 = (input("Masukan Angka pertama: "))
        bianAngka2 = (input("Masukan Angka kedua: "))
        if (bianAngka1.replace('.','',1).isdigit() and bianAngka2.replace('.','',1).isdigit()):
            bianAngka1 = float(bianAngka1)
            bianAngka2 = float(bianAngka2)
            bianHitung = bianAngka1 + bianAngka2
            print(f"{bianAngka1} + {bianAngka2} = {bianHitung}")
        else:
            print("MASUKAN ANGKA DAN BUKAN HURUF!")

    elif BianPilih == 2:
        print("Anda Memilih Tambah")
        bianAngka1 = (input("Masukan Angka pertama: "))
        bianAngka2 = (input("Masukan Angka kedua: "))
        if (bianAngka1.replace('.', '', 2).isdigit() and bianAngka2.replace('.', '', 2).isdigit()):
            bianAngka1 = float(bianAngka1)
            bianAngka2 = float(bianAngka2)
            bianHitung = bianAngka1 - bianAngka2
            print(f"{bianAngka1} - {bianAngka2} = {bianHitung}")
        else:
            print("MASUKAN ANGKA DAN BUKAN HURUF!")
    elif BianPilih == 3:
        print("Anda Memilih Tambah")
        bianAngka1 = (input("Masukan Angka pertama: "))
        bianAngka2 = (input("Masukan Angka kedua: "))
        if (bianAngka1.replace('.', '', 3).isdigit() and bianAngka2.replace('.', '', 3).isdigit()):
            bianAngka1 = float(bianAngka1)
            bianAngka2 = float(bianAngka2)
            bianHitung = bianAngka1 * bianAngka2
            print(f"{bianAngka1} x {bianAngka2} = {bianHitung}")
        else:
            print("MASUKAN ANGKA DAN BUKAN HURUF!")
    elif BianPilih == 4:
        print("Anda Memilih Tambah")
        bianAngka1 = (input("Masukan Angka pertama: "))
        bianAngka2 = (input("Masukan Angka kedua: "))
        if (bianAngka1.replace('.', '', 4).isdigit() and bianAngka2.replace('.', '', 4).isdigit()):
            bianAngka1 = float(bianAngka1)
            bianAngka2 = float(bianAngka2)
            bianHitung = bianAngka1 / bianAngka2
            print(f"{bianAngka1} : {bianAngka2} = {bianHitung}")
        else:
            print("MASUKAN ANGKA DAN BUKAN HURUF!")
    elif BianPilih == 5:
        print("Keluar Program")
        break
    else:
        print("MASUKAN INPUTAN YANG BENAR (1/2/3/4/5)")


