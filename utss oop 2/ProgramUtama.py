from Perpustakaan import perpusatakaan, katalog_perpustakaan

sistemPerpusatakaan = perpusatakaan(nama_cabang="pusat")

while True:
    print("=====Daftar Menu=====")
    print("1. Tampilkan daftar buku")
    print("2. Pinjam buku")
    print("3. Kembalikan buku")
    print("4. Exit")

    pilihan = input("Pilihan Menu(1-4): ")

    if pilihan == '1':
        sistemPerpusatakaan.show_katalog(katalog_perpustakaan)

    elif pilihan == '2':
        id_buku= input("Masukkan ID buku yang ingin dipinjam: ")
        sistemPerpusatakaan.peminjaman(id_buku, katalog_perpustakaan)

    elif pilihan == '3':
        id_buku = input("Masukkan ID buku yang ingin dikembalikan: ")
        tgl_pinjam = input("Masukkan tanggal pinjam (YYYY-MM-DD): ")
        tgl_kembali = input("Masukkan tanggal kembali (YYYY-MM-DD): ")
        sistemPerpusatakaan.pengembalian(katalog_perpustakaan, id_buku, tgl_pinjam, tgl_kembali)
   
    elif pilihan == '4':
        print("Terima kasih telah menggunakan sistem perpustakaan!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")