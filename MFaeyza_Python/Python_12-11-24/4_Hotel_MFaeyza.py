print("Pilih Jenis Kamar Hotel:")
print("1.Kamar Standard (300k)")
print("2.Kamar Deluxe (500K)")
print("3.Kamar Suite (800k)")
kamarBian = int(input("Pilih kamar hotel mu 1-3: "))
hariBian = int (input("Berapa hari kamu akan menginap: "))
if kamarBian == 1:
    print("Kamu memilih kamar standard (300k)")
    print("Kamu menginap selama ", hariBian,"Hari")
    hargaBian = 300000
    if hariBian > 3:
        print("Karena kamu menginap lebih dari 3 hari mendapatkan diskon sebesar 5%")
        hargahariBian = hargaBian * hariBian
        diskonBian = hargahariBian * 0.05
    else:
        print("Karena kamu menginap tidak lebih dari 3 hari tidak dapat diskon")
        diskonBian = 0
elif kamarBian == 2:
    print("Kamu memilih kamar Deluxe (500k)")
    print("Kamu menginap selama ", hariBian,"Hari")
    hargaBian = 500000
    if hariBian > 5:
        print("Karena kamu menginap lebih dari 5 hari mendapatkan diskon sebesar 10%")
        hargahariBian = hargaBian * hariBian
        diskonBian = hargahariBian * 0.1
    else:
        print("Karena kamu menginap tidak lebih dari 3 hari tidak dapat diskon")
        diskonBian = 0
elif kamarBian == 3:
    print("Kamu memilih kamar Suite (800k)")
    print("Kamu menginap selama ", hariBian,"Hari")
    hargaBian = 800000
    if hariBian > 7:
        print("Karena kamu menginap lebih dari 7 hari mendapatkan diskon sebesar 10%")
        hargahariBian = hargaBian * hariBian
        diskonBian = hargahariBian * 0.15
    else:
        print("Karena kamu menginap tidak lebih dari 3 hari tidak dapat diskon")
        diskonBian = 0
else:
    print("Kamar tidak valid (1-3")

totalBian = hargahariBian - diskonBian
print ("Jadi kamu harus membayar sebesar: rp.", totalBian)
print("Menginap selama:", hariBian ,"Hari")