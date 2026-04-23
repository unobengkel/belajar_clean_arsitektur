from abc import ABC, abstractmethod
from typing import Optional, List
from domain.entities.entity_barang import Barang


class IBarangRepository(ABC):
    """Interface repository untuk entity Barang."""

    @abstractmethod
    def simpan(self, entity: Barang) -> Barang:
        """Menyimpan data barang baru."""
        pass

    @abstractmethod
    def update(self, entity: Barang) -> Barang:
        """Memperbarui data barang."""
        pass

    @abstractmethod
    def hapus(self, id: int) -> None:
        """Menghapus data barang berdasarkan id."""
        pass

    @abstractmethod
    def cari_by_id(self, id: int) -> Optional[Barang]:
        """Mencari barang berdasarkan id."""
        pass

    @abstractmethod
    def cari_semua(self) -> List[Barang]:
        """Mengambil semua data barang."""
        pass

    @abstractmethod
    def cari_by_nama(self, nama: str) -> List[Barang]:
        """Mencari barang berdasarkan nama (partial match)."""
        pass

    @abstractmethod
    def cari_by_idjenis(self, idjenis: int) -> List[Barang]:
        """Mencari barang berdasarkan id jenis."""
        pass

    @abstractmethod
    def cari_by_idmerek(self, idmerek: int) -> List[Barang]:
        """Mencari barang berdasarkan id merek."""
        pass
