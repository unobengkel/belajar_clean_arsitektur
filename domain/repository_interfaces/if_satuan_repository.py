from abc import ABC, abstractmethod
from typing import Optional, List
from domain.entities.entity_satuan import Satuan


class ISatuanRepository(ABC):
    """Interface repository untuk entity Satuan."""

    @abstractmethod
    def simpan(self, entity: Satuan) -> Satuan:
        """Menyimpan data satuan baru."""
        pass

    @abstractmethod
    def update(self, entity: Satuan) -> Satuan:
        """Memperbarui data satuan."""
        pass

    @abstractmethod
    def hapus(self, id: int) -> None:
        """Menghapus data satuan berdasarkan id."""
        pass

    @abstractmethod
    def cari_by_id(self, id: int) -> Optional[Satuan]:
        """Mencari satuan berdasarkan id."""
        pass

    @abstractmethod
    def cari_semua(self) -> List[Satuan]:
        """Mengambil semua data satuan."""
        pass

    @abstractmethod
    def cari_by_nama(self, nama: str) -> Optional[Satuan]:
        """Mencari satuan berdasarkan nama."""
        pass
