from typing import Optional


class DTOBarang:
    """Data Transfer Object untuk Barang."""

    def __init__(
        self,
        id: int = 0,
        idjenis: int = 0,
        idmerek: int = 0,
        idsatuan: int = 0,
        nama: str = "",
        nama_jenis: Optional[str] = None,
        nama_merek: Optional[str] = None,
        nama_satuan: Optional[str] = None,
        jumlah_stok: int = 0,
    ):
        self.id = id
        self.idjenis = idjenis
        self.idmerek = idmerek
        self.idsatuan = idsatuan
        self.nama = nama
        self.nama_jenis = nama_jenis
        self.nama_merek = nama_merek
        self.nama_satuan = nama_satuan
        self.jumlah_stok = jumlah_stok

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "idjenis": self.idjenis,
            "idmerek": self.idmerek,
            "idsatuan": self.idsatuan,
            "nama": self.nama,
            "nama_jenis": self.nama_jenis,
            "nama_merek": self.nama_merek,
            "nama_satuan": self.nama_satuan,
            "jumlah_stok": self.jumlah_stok,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "DTOBarang":
        return cls(
            id=data.get("id", 0),
            idjenis=data.get("idjenis", 0),
            idmerek=data.get("idmerek", 0),
            idsatuan=data.get("idsatuan", 0),
            nama=data.get("nama", ""),
            nama_jenis=data.get("nama_jenis"),
            nama_merek=data.get("nama_merek"),
            nama_satuan=data.get("nama_satuan"),
            jumlah_stok=data.get("jumlah_stok", 0),
        )

    def __repr__(self) -> str:
        return f"DTOBarang(id={self.id}, nama='{self.nama}')"
