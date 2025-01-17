while True:
    print("MENU " + "\n" + "1. Luas Segitiga " + "\n" + "2. Luas Lingkaran " + "\n" + "Pilih Menu (1/2). ")
    try:
        menuBian = int(input())
        if menuBian == 1:
            print("Kamu memilih luas segitiga dengan rumus : 1/2 * alas * tinggi " + "\n" + "Masukan nilai alas")
            alasBian = int(input())
            print("Masukan nilai tinggi")
            tinggiBian = int(input())
            luasSegi3Bian = float(1 / 2 * alasBian * tinggiBian)
            print("Jadi rumus luas segitiga adalah: " + "\n" + "1/2 * " + str(alasBian) + " * " + str(tinggiBian) + " = " + str(luasSegi3Bian))
        elif menuBian == 2:
            print("Kamu memilih luas lingkaran dengan rumus : phi * r * r " + "\n" + "Masukan nilai r(jari-jari)")
            rBian = int(input())
            luaslingkaranBian =float(3.14 * rBian * rBian) 
            print("Jadi rumus luas lingkaran adalah: " + "\n" + "3.14 * " + str(rBian) + " * " + str(rBian) + " = " + str(luaslingkaranBian))
        else:
            print("Pilih (1/2)")
            continue
        break
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
    pilihanBian = input().lower()
    if pilihanBian not in ['y', 't']:
        print("Pilihan hanya (Y/T)")
    else:
        if pilihanBian == 't':
            break
        else:
            # Jika 'y', ulangi loop utama
            continue