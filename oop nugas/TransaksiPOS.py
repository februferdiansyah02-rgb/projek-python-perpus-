from PajakPPN import pajakPPN

class TransaksiPOS(pajakPPN):
    def __init__(self, pelanggan, meja):
        super().__init__(0)
        self.pelanggan = pelanggan
        self.meja = meja
        self.daftar_pesanan = []

    def tambah_item(self, nama_makanan, harga, jumlah): 
        total_item = jumlah * harga
        item = {
            "nama": nama_makanan,
            "jumlah": jumlah,
            "harga": harga,
            "total_item": total_item
        }
        self.daftar_pesanan.append(item)
        self.subtotal += total_item 
        self.hitung_pajak()
        return self.daftar_pesanan

    def cetak_struk(self):
        print("="*30)
        print(f"STRUK PEMBAYARAN - Meja {self.meja}") 
        print("="*30)
        print(f"Pelanggan: {self.pelanggan}")
        print("-"*30)
        for item in self.daftar_pesanan:
            print(f"{item['nama']}  x{item['jumlah']}  Rp {item['total_item']}")
        print("-"*30)
        print(f"Subtotal    : Rp {self.subtotal}")
        print(f"Pajak (10%) : Rp {self.nilai_pajak}")
        print(f"Total Akhir : Rp {self.total_akhir}")
        print("="*30)

    def proses_pembayaran(self):
        bayar = float(input("Masukkan jumlah pembayaran: "))
        if bayar > self.total_akhir:
            kembalian = bayar - self.total_akhir
            print(f"Pembayaran berhasil. Kembalian: {kembalian}")
        elif bayar < self.total_akhir:
            print(f"Pembayaran kurang. Kekurangan: {self.total_akhir - bayar}")
            if input("Bayar kekurangan sekarang? (y/n): ").lower() == 'y':
                self.proses_pembayaran() 
                if bayar > self.total_akhir:
                    kembalian = bayar - self.total_akhir
                    print(f"Pembayaran berhasil. Kembalian: {kembalian}")
                elif bayar < self.total_akhir:
                    print(f"Pembayaran masih kurang. Transaksi dibatalkan.")
                else:
                    print("Pembayaran pas, terima kasih!")        
        else:                                                                                                                        
            print("Pembayaran pas, terima kasih!")                                                                                                                                                                                                      



