class DTOMerek:
    """Data Transfer Object untuk Merek."""

    def __init__(self, id: int = 0, nama: str = ""):
        self.id = id
        self.nama = nama

    def to_dict(self) -> dict:
        return {"id": self.id, "nama": self.nama}

    @classmethod
    def from_dict(cls, data: dict) -> "DTOMerek":
        return cls(id=data.get("id", 0), nama=data.get("nama", ""))

    def __repr__(self) -> str:
        return f"DTOMerek(id={self.id}, nama='{self.nama}')"
