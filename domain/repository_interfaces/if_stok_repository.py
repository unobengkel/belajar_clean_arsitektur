from abc import ABC, abstractmethod
from typing import Optional, List
from domain.entities.entity_stok import Stok


class IStokRepository(ABC):
    """Interface repository untuk entity Stok."""

    @abstractmethod
    def simpan(self, entity: Stok) -> Stok:
        """Menyimpan data stok baru."""
        pass

    @abstractmethod
    def update(self, entity: Stok) -> Stok:
        """Memperbarui data stok."""
        pass

    @abstractmethod
    def hapus(self, id: int) -> None:
        """Menghapus data stok berdasarkan id."""
        pass

    @abstractmethod
    def cari_by_id(self, id: int) -> Optional[Stok]:
        """Mencari stok berdasarkan id."""
        pass

    @abstractmethod
    def cari_semua(self) -> List[Stok]:
        """Mengambil semua data stok."""
        pass

    @abstractmethod
    def cari_by_idbarang(self, idbarang: int) -> Optional[Stok]:
        """Mencari stok berdasarkan id barang."""
        pass
