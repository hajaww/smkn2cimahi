mtkBian=int(input("masukan nilai mtk"))
fisikaBian=int(input("masukan nilai fisika"))
inggrisBian=int(input("masukan nilai inggris"))
seniBian=int(input("masukan nilai seni"))
sejarahBian=int(input("masukan nilai sejarah"))
if mtkBian > 80 and fisikaBian > 75 or inggrisBian > 85:
    print("Anda diterima di studi teknik")
elif seniBian > 70 or sejarahBian > 80:
    print("Anda diterima di studi seni")
else :
    print("Anda tidak diterima di program studi apapun")