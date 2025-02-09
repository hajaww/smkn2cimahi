def input_nama():
    print("=== Aplikasi Input Nama ===")

    try:
        jumlah = int(input("Masukan jumlah nama yang ingin diimput: "))

        if jumlah < 1:
            print("Jumlah nama harus lebih dari 0!")
            return

        nama_list = []
        for i in range (1, jumlah + 1):
            nama = input(f"Masukkan nama ke-{i}: ")
            nama_list.append(nama)

        print("\n === Hasil Nama yang Diimputkan ===")
        for i, nama in enumerate(nama_list, start=1):
            print(f"Nama {i}: {nama}")

    except ValueError:
        print("Input tidak valid. Harap masukan angka untuk jumlah nama.")

if __name__ == "__main__":
    input_nama()