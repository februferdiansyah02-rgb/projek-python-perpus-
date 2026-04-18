from KomponenHarga import komponenHarga
class pajakPPN(komponenHarga):
    def __init__(self, subtotal):
        super ().__init__(subtotal)
        self.hitung_pajak()
        
    def hitung_pajak(self):
        self.nilai_pajak = self.subtotal * 0.10
        self.total_akhir = self.subtotal + self.nilai_pajak 