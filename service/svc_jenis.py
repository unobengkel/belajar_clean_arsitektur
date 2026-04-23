from typing import Optional, List
from domain.repository_interfaces.if_jenis_repository import IJenisRepository
from domain.entities.entity_jenis import Jenis
from data.dto.dto_jenis import DTOJenis


class SvcJenis:
    """Service / Use Case untuk Jenis Barang."""

    def __init__(self, repo: IJenisRepository):
        self._repo = repo

    def tambah(self, nama: str) -> DTOJenis:
        """Menambahkan jenis baru."""
        existing = self._repo.cari_by_nama(nama)
        if existing:
            raise ValueError(f"Jenis '{nama}' sudah ada.")
        entity = Jenis(id=0, nama=nama)
        hasil = self._repo.simpan(entity)
        return DTOJenis(id=hasil.id, nama=hasil.nama)

    def ubah(self, id: int, nama_baru: str) -> DTOJenis:
        """Mengubah nama jenis."""
        existing = self._repo.cari_by_id(id)
        if not existing:
            raise ValueError(f"Jenis dengan id {id} tidak ditemukan.")
        existing.nama = nama_baru
        hasil = self._repo.update(existing)
        return DTOJenis(id=hasil.id, nama=hasil.nama)

    def hapus(self, id: int) -> None:
        """Menghapus jenis berdasarkan id."""
        existing = self._repo.cari_by_id(id)
        if not existing:
            raise ValueError(f"Jenis dengan id {id} tidak ditemukan.")
        self._repo.hapus(id)

    def cari_by_id(self, id: int) -> Optional[DTOJenis]:
        """Mencari jenis berdasarkan id."""
        entity = self._repo.cari_by_id(id)
        if entity:
            return DTOJenis(id=entity.id, nama=entity.nama)
        return None

    def semua(self) -> List[DTOJenis]:
        """Mendapatkan semua jenis."""
        entities = self._repo.cari_semua()
        return [DTOJenis(id=e.id, nama=e.nama) for e in entities]
