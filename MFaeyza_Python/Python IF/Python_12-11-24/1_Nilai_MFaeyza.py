nilaiBian = int(input("Masukan nilai yang diperoleh :"))
if nilaiBian > 85 and nilaiBian <= 100:
    print ("Lulus dengan predikat sangat baik")
elif nilaiBian >= 70 and nilaiBian <= 85:
    print ("Lulus dengan predikat baik")
elif nilaiBian < 70:
    if nilaiBian < 50:
        print("Kamu harus melakukan remedial")
    else:
        print("Kamu harus melakukan ujian ulang")
else:
    print("Rentang nilai 0-100")

