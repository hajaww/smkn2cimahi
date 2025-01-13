biantahunlahir = int(input("Masukan Tahun Lahir Fara: "))
biantahunsaatini = 0
while biantahunsaatini <= biantahunlahir :
    biantahunsaatini = int(input("Masukan thaun saat ini"))
    if biantahunsaatini <= biantahunlahir:
        print("Tahun yg dimasukan tidak valid")
bianumur= biantahunsaatini - biantahunlahir
print("Umur Fara adalah;",bianumur,"Tahun")
