class Satuan:
    """Entity untuk Satuan Barang."""

    def __init__(self, id: int = 0, nama: str = ""):
        self._id = id
        self._nama = nama

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def nama(self) -> str:
        return self._nama

    @nama.setter
    def nama(self, value: str):
        self._nama = value

    def __repr__(self) -> str:
        return f"Satuan(id={self._id}, nama='{self._nama}')"
