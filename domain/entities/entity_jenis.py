class Jenis:
    """Entity Jenis Barang."""

    def __init__(self, id: int = 0, nama: str = ""):
        self.id = id
        self.nama = nama

    def __repr__(self) -> str:
        return f"Jenis(id={self.id}, nama='{self.nama}')"
