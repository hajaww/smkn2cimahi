#Menentukan Grading dengan elif
namamapel1 = str(input("Masukan nama mapel pertama"))
nilai1 = float(input("Masukan Nilai mapel " +namamapel1))
namamapel2 = str(input("Masukan nama mapel kedua"))
nilai2 = float(input("Masukan Nilai mapel " +namamapel2))
namamapel3 = str(input("Masukan nama mapel ketiga"))
nilai3 = float(input("Masukan Nilai mapel ketiga " +namamapel3))
RataBian = (nilai1 + nilai2 + nilai3) / 3
print ("Rata-Ratanya adalah" ,RataBian)
if RataBian >= 91 and RataBian <=100:
    print("Grade A")
elif RataBian >= 81 and RataBian <=90:
    print("Grade B")
elif RataBian >= 71 and RataBian <=80:
    print("Grade C")
elif RataBian >= 61 and RataBian <=70:
    print("Grade D")
elif RataBian < 61 :
    print("Grade E")
else:
    print ("Rentang nilai antara 0-100")