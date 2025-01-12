bianAngka = int(input("Masukan Angka genap atau ganjil: "))
bianTotalGenap = 0
bianTotalGanjil = 0
bianAngka2 = 1
while bianAngka2 <= bianAngka:
    if bianAngka % 2 == 0:
        bianTotalGenap += bianAngka
    else:
        bianTotalGanjil += bianAngka
    bianAngka -= bianAngka2
print("Jadi penjumlahan angka genap adalah ", bianTotalGenap )
print("Jadi penjumlahan angka ganjil adalah ", bianTotalGanjil )


