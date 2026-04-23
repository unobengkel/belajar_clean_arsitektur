class DTOStok:
    """Data Transfer Object untuk Stok."""

    def __init__(
        self,
        id: int = 0,
        idbarang: int = 0,
        jumlah: int = 0,
        last_timeupdate: str = "",
        nama_barang: str = "",
    ):
        self.id = id
        self.idbarang = idbarang
        self.jumlah = jumlah
        self.last_timeupdate = last_timeupdate
        self.nama_barang = nama_barang

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "idbarang": self.idbarang,
            "jumlah": self.jumlah,
            "last_timeupdate": self.last_timeupdate,
            "nama_barang": self.nama_barang,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "DTOStok":
        return cls(
            id=data.get("id", 0),
            idbarang=data.get("idbarang", 0),
            jumlah=data.get("jumlah", 0),
            last_timeupdate=data.get("last_timeupdate", ""),
            nama_barang=data.get("nama_barang", ""),
        )

    def __repr__(self) -> str:
        return f"DTOStok(id={self.id}, idbarang={self.idbarang}, jumlah={self.jumlah})"
