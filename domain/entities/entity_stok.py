class Stok:
    """Entity untuk Stok Barang."""

    def __init__(self, id: int, idbarang: int, jumlah: int, last_timeupdate: str):
        self._id = id
        self._idbarang = idbarang
        self._jumlah = jumlah
        self._last_timeupdate = last_timeupdate

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def idbarang(self) -> int:
        return self._idbarang

    @idbarang.setter
    def idbarang(self, value: int):
        self._idbarang = value

    @property
    def jumlah(self) -> int:
        return self._jumlah

    @jumlah.setter
    def jumlah(self, value: int):
        self._jumlah = value

    @property
    def last_timeupdate(self) -> str:
        return self._last_timeupdate

    @last_timeupdate.setter
    def last_timeupdate(self, value: str):
        self._last_timeupdate = value

    def __repr__(self) -> str:
        return f"Stok(id={self._id}, idbarang={self._idbarang}, jumlah={self._jumlah}, last_timeupdate='{self._last_timeupdate}')"
