from typing import Optional, List
from domain.repository_interfaces.if_merek_repository import IMerekRepository
from domain.entities.entity_merek import Merek
from data.dto.dto_merek import DTOMerek


class SvcMerek:
    """Service / Use Case untuk Merek Barang."""

    def __init__(self, repo: IMerekRepository):
        self._repo = repo

    def tambah(self, nama: str) -> DTOMerek:
        existing = self._repo.cari_by_nama(nama)
        if existing:
            raise ValueError(f"Merek '{nama}' sudah ada.")
        entity = Merek(id=0, nama=nama)
        hasil = self._repo.simpan(entity)
        return DTOMerek(id=hasil.id, nama=hasil.nama)

    def ubah(self, id: int, nama_baru: str) -> DTOMerek:
        existing = self._repo.cari_by_id(id)
        if not existing:
            raise ValueError(f"Merek dengan id {id} tidak ditemukan.")
        existing.nama = nama_baru
        hasil = self._repo.update(existing)
        return DTOMerek(id=hasil.id, nama=hasil.nama)

    def hapus(self, id: int) -> None:
        existing = self._repo.cari_by_id(id)
        if not existing:
            raise ValueError(f"Merek dengan id {id} tidak ditemukan.")
        self._repo.hapus(id)

    def cari_by_id(self, id: int) -> Optional[DTOMerek]:
        entity = self._repo.cari_by_id(id)
        if entity:
            return DTOMerek(id=entity.id, nama=entity.nama)
        return None

    def semua(self) -> List[DTOMerek]:
        entities = self._repo.cari_semua()
        return [DTOMerek(id=e.id, nama=e.nama) for e in entities]
