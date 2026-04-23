from abc import ABC, abstractmethod
from typing import Optional, List
from domain.entities.entity_jenis import Jenis


class IJenisRepository(ABC):
    """Interface repository untuk entity Jenis."""

    @abstractmethod
    def simpan(self, entity: Jenis) -> Jenis:
        """Menyimpan data jenis baru."""
        pass

    @abstractmethod
    def update(self, entity: Jenis) -> Jenis:
        """Memperbarui data jenis."""
        pass

    @abstractmethod
    def hapus(self, id: int) -> None:
        """Menghapus data jenis berdasarkan id."""
        pass

    @abstractmethod
    def cari_by_id(self, id: int) -> Optional[Jenis]:
        """Mencari jenis berdasarkan id."""
        pass

    @abstractmethod
    def cari_semua(self) -> List[Jenis]:
        """Mengambil semua data jenis."""
        pass

    @abstractmethod
    def cari_by_nama(self, nama: str) -> Optional[Jenis]:
        """Mencari jenis berdasarkan nama."""
        pass
