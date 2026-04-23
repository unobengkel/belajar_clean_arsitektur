class Barang:
    """Entity untuk Barang."""

    def __init__(self, id: int, idjenis: int, idmerek: int, idsatuan: int, nama: str):
        self._id = id
        self._idjenis = idjenis
        self._idmerek = idmerek
        self._idsatuan = idsatuan
        self._nama = nama

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def idjenis(self) -> int:
        return self._idjenis

    @idjenis.setter
    def idjenis(self, value: int):
        self._idjenis = value

    @property
    def idmerek(self) -> int:
        return self._idmerek

    @idmerek.setter
    def idmerek(self, value: int):
        self._idmerek = value

    @property
    def idsatuan(self) -> int:
        return self._idsatuan

    @idsatuan.setter
    def idsatuan(self, value: int):
        self._idsatuan = value

    @property
    def nama(self) -> str:
        return self._nama

    @nama.setter
    def nama(self, value: str):
        self._nama = value

    def __repr__(self) -> str:
        return f"Barang(id={self._id}, nama='{self._nama}', idjenis={self._idjenis}, idmerek={self._idmerek}, idsatuan={self._idsatuan})"
