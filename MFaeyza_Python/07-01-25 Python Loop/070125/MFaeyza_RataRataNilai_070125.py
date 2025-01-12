mapelBian = 0
totalBian = 0
while mapelBian <= 4:
    nilaiBian = int(input("Masukan Nilai Mata Pelajaran:"))
    totalBian += nilaiBian
    mapelBian += 1
    if mapelBian == 4:
        break
nilaiBian = totalBian / 4
print("Jadi nilai rata-ratanya adalah:",nilaiBian)

