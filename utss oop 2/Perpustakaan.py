from datetime import datetime

from Buku import buku

class perpusatakaan(buku):
    def __init__ (self, nama_cabang='pusat'):
        super().__init__(item_id=None, judul=None, penulis=None)
        self.nama_cabang = nama_cabang

    def show_katalog(self, katalog):
        print("=" * 70)
        print("ID\t| JUDUL BUKU\t\t| PENULIS\t\t| STATUS")
        print("-" * 70)
        for id_buku, data in katalog.items():
            buku = data['item']
            status_teks = "[Tersedia]" if data["tersedia"] else "[Dipinjam]"
            print(f"{id_buku}\t| {buku.get_judul()[:15]:<15}\t| {buku.get_penulis()[:15]:<15}\t| {status_teks }")
        print("=" * 70)

    def peminjaman(self, item_id, katalog):
        if item_id in katalog:
            data = katalog[item_id]
            buku = data['item']

            if data['tersedia']:
                data['tersedia'] = False
                buku.set_status(False)
                print(f"[SUKSES] Berhasil meminjam {buku.get_judul()}")
                return True
            else:
                print(f"[GAGAL] Buku {buku.get_judul()} sedang dipinjam.")
        else:
            print(f"[GAGAL] Buku dengan ID {item_id} tidak ditemukan.")
        return False
    
    def pengembalian(self, katalog, item_id, tgl_pinjam, tgl_kembali):
        if item_id in katalog:
            data = katalog[item_id]
            buku = data['item']
            
            if data['tersedia']:
                print(f"[GAGAL] Buku {buku.get_judul()} sudah tersedia di perpusataan.")
                return False
            
            fmt = "%Y-%m-%d"
            d1 = datetime.strptime(tgl_pinjam, fmt)
            d2 = datetime.strptime(tgl_kembali, fmt)
            durasi = (d2 - d1).days

            print(f"[SUSKES] pengembalian: {buku.get_judul()}")
            print(f"Total durasi: {durasi} (Batas: 7 hari)")

            if durasi > 7:
                terlambat = durasi - 7
                total_denda = buku.hitung_denda(terlambat) 
                print(f"Terlambat: {terlambat} hari. TOTAL DENDA: Rp {total_denda}")
            else:
                print("Tidak ada denda. Terima kasih telah mengembalikan tepat waktu.")

            data['tersedia'] = True
            buku.set_status(True)
            return True
        else:
            print(f"[GAGAL] Buku dengan ID {item_id} tidak ditemukan.")
            return False

katalog_perpustakaan = {
    "B01": {"item": buku("B01", "Filosofi Teras", "Henry Manampiring"), "tersedia": True},
    "B02": {"item": buku("B02", "Laskar Pelangi", "Andrea Hirata"), "tersedia": True},
    "B03": {"item": buku("B03", "Bumi Manusia", "Pramoedya Ananta Toer"), "tersedia": True},
    "B04": {"item": buku("B04", "Negeri 5 Menara", "A. Fuadi"), "tersedia": True},
    "B05": {"item": buku("B05", "Cantik Itu Luka", "Eka Kurniawan"), "tersedia": True},
    "B06": {"item": buku("B06", "Pulang", "Leila S. Chudori"), "tersedia": True},
    "B07": {"item": buku("B07", "Hujan Bulan Juni", "Sapardi Djoko Damono"), "tersedia": True},
    "B08": {"item": buku("B08", "Garis Waktu", "Fiersa Besari"), "tersedia": True},
} 


