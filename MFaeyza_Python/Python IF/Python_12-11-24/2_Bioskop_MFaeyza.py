# noinspection PyInterpreter
usiaBian = int(input("Masukan usia anda"))
print ("1.Hari senin")
print ("2.Hari selasa")
print ("3.Hari rabu")
print ("4.Hari kamis")
print ("5.Hari jumat")
print ("6.Hari sabtu")
print ("7.Hari minggu")
hariBian = int(input("pilih hari 1-7"))

if hariBian <=6 or hariBian >= 7:
    if usiaBian < 12 or usiaBian > 60:
        hargaBian = 70000
        diskonBian = 0.5

    else:
        hargaBian = 70000
        diskonBian = 1
elif hariBian < 6:
    if usiaBian < 12 or usiaBian > 60:
        hargaBian = 50000
        diskonBian = 0.5

    else:
        hargaBian = 50000
        diskonBian = 1
else:
    print("Masukan inputan yang valid")

totalbian = hargaBian * diskonBian
print("Jadi total pembayaran sebesarp rp.",totalbian)


