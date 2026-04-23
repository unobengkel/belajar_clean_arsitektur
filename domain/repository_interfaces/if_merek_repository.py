from abc import ABC, abstractmethod
from typing import Optional, List
from domain.entities.entity_merek import Merek


class IMerekRepository(ABC):
    """Interface repository untuk entity Merek."""

    @abstractmethod
    def simpan(self, entity: Merek) -> Merek:
        """Menyimpan data merek baru."""
        pass

    @abstractmethod
    def update(self, entity: Merek) -> Merek:
        """Memperbarui data merek."""
        pass

    @abstractmethod
    def hapus(self, id: int) -> None:
        """Menghapus data merek berdasarkan id."""
        pass

    @abstractmethod
    def cari_by_id(self, id: int) -> Optional[Merek]:
        """Mencari merek berdasarkan id."""
        pass

    @abstractmethod
    def cari_semua(self) -> List[Merek]:
        """Mengambil semua data merek."""
        pass

    @abstractmethod
    def cari_by_nama(self, nama: str) -> Optional[Merek]:
        """Mencari merek berdasarkan nama."""
        pass
