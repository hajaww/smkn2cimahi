print("=== Aplikasi Reservasi Kamarung's Hotel ===")
bianNama = str(input("Masukan Nama Tamu: "))
print("Jenis Kamar: ")
print("1. Standard - Rp 300.000/malam ")
print("2. Deluxe - Rp 500.000/malam ")
print("3. Suite - Rp 800.000/malam ")
bianKamar = str(input("Pilih Jenis Kamar: Standard/Deluxe/Suite "))
bianMalam = int(input("Berapa Lama kamu akan menginap? "))
if bianKamar == "Standard" or bianKamar == "standard":
    print("Kamu memilih kamar Standard dengan harga Rp 300.000/Malam")
    bianHarga = 300000
elif bianKamar == "Deluxe" or bianKamar == "deluxe":
    print("Kamu memilih kamar Deluxe dengan harga Rp 500.000/Malam")
    bianHarga = 500000
elif bianKamar == "Suite" or bianKamar == "suite":
    print("Kamu memilih kamar Suite dengan harga Rp 800.000/Malam")
    bianHarga = 800000
else:
    print("Kamar Tidak Valid")

bianTotal = bianHarga * bianMalam
if bianTotal >= 2000000:
    print("Karena pembelian anda lebih atau sama dengan Rp - 2.000.000 anda, anda mendapatkan diskon sebesar 10%")
    bianDiskon= 0.1
    bianDiskonOut= "10%"
else:
    print("Maaf kamu tidak dapat diskon")
    bianDiskon = 0
    bianDiskonOut = "0"

bianDiskon = bianTotal * bianDiskon
bianSetelahPotong = bianTotal - bianDiskon
bianPajak = bianSetelahPotong * 0.1
bianTotalKeseluruhan = bianSetelahPotong + bianPajak
print("")
print("=== Detail Reservasi ===")
print("Nama Tamu: "+bianNama)
print("Jenis Kamar: "+bianKamar)
print("Harga Per Malam: Rp.",bianHarga)
print("Jumlah Malam: ",bianMalam)
print("Total sebelum diskon: Rp.",bianTotal)

print("Diskon: Rp.",bianDiskon)
print("Total setelah diskon: Rp.",bianSetelahPotong)
print("Pajak(10%): Rp.",bianPajak)
print("Total Biaya: Rp.",bianTotalKeseluruhan)
print("")
print("=== Pecahan Uang ===")
while  bianTotalKeseluruhan > 1000:
    if bianTotalKeseluruhan >= 100000:
        bianLembar = bianTotalKeseluruhan // 100000
        bianSisa= bianTotalKeseluruhan % 100000
        print("Lembar Rp.100.000: ", bianLembar)
    elif bianTotalKeseluruhan >= 50000:
        bianLembar = bianTotalKeseluruhan // 50000
        bianSisa = bianTotalKeseluruhan % 50000
        print("Lembar Rp.50.000: ", bianLembar)
    elif bianTotalKeseluruhan >= 20000:
        bianLembar = bianTotalKeseluruhan // 20000
        bianSisa = bianTotalKeseluruhan % 20000
        print("Lembar Rp.20.000: ", bianLembar)
    elif bianTotalKeseluruhan >= 10000:
        bianLembar = bianTotalKeseluruhan // 10000
        bianSisa = bianTotalKeseluruhan % 10000
        print("Lembar Rp.10.000: ", bianLembar)
    elif bianTotalKeseluruhan >= 5000:
        bianLembar = bianTotalKeseluruhan // 5000
        bianSisa = bianTotalKeseluruhan % 5000
        print("Lembar Rp.100.000: ", bianLembar)
    elif bianTotalKeseluruhan >= 2000:
        bianLembar = bianTotalKeseluruhan // 2000
        bianSisa = bianTotalKeseluruhan % 2000
        print("Lembar Rp.2.000: ", bianLembar)
    elif bianTotalKeseluruhan >= 1000:
        bianLembar = bianTotalKeseluruhan // 1000
        bianSisa = bianTotalKeseluruhan % 1000
        print("Lembar Rp.1.000: ", bianLembar)
    bianTotalKeseluruhan = bianSisa