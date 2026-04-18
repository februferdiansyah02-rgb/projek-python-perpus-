from TransaksiPOS import TransaksiPOS

# PROGRAM UTAMA
pelanggan = input("Masukkan nama pelanggan: ")
meja = input("Masukkan nomor meja: ")

transaksi = TransaksiPOS(pelanggan, meja)

while True:
    nama_makanan = input("Masukkan nama makanan (atau 'selesai' untuk selesai): ")
    if nama_makanan.lower() == 'selesai':
        break
    harga = float(input("Masukkan harga makanan: "))
    jumlah = int(input("Masukkan jumlahnya: "))
    transaksi.tambah_item(nama_makanan, harga, jumlah)

transaksi.cetak_struk()
transaksi.proses_pembayaran()