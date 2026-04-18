class buku:
    def __init__(self, item_id, judul, penulis, status=True):
        self._item_id = item_id
        self._judul = judul
        self._penulis = penulis
        self._status = True

    def get_item_id(self):
        return self._item_id

    def get_judul(self):
        return self._judul

    def get_penulis(self):
        return self._penulis

    def get_status(self):
        return self._status
    
    def set_item_id(self, item_id):
        self._item_id = item_id

    def set_judul(self, judul):
        self._judul = judul

    def set_penulis(self, penulis):
        self._penulis = penulis

    def set_status(self, status):
        self._status = status

    def hitung_denda(self, hari_terlambat):
        return hari_terlambat * 2000