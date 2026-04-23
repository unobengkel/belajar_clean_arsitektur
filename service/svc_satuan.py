from typing import Optional, List
from domain.repository_interfaces.if_satuan_repository import ISatuanRepository
from domain.entities.entity_satuan import Satuan
from data.dto.dto_satuan import DTOSatuan


class SvcSatuan:
    """Service / Use Case untuk Satuan Barang."""

    def __init__(self, repo: ISatuanRepository):
        self._repo = repo

    def tambah(self, nama: str) -> DTOSatuan:
        existing = self._repo.cari_by_nama(nama)
        if existing:
            raise ValueError(f"Satuan '{nama}' sudah ada.")
        entity = Satuan(id=0, nama=nama)
        hasil = self._repo.simpan(entity)
        return DTOSatuan(id=hasil.id, nama=hasil.nama)

    def ubah(self, id: int, nama_baru: str) -> DTOSatuan:
        existing = self._repo.cari_by_id(id)
        if not existing:
            raise ValueError(f"Satuan dengan id {id} tidak ditemukan.")
        existing.nama = nama_baru
        hasil = self._repo.update(existing)
        return DTOSatuan(id=hasil.id, nama=hasil.nama)

    def hapus(self, id: int) -> None:
        existing = self._repo.cari_by_id(id)
        if not existing:
            raise ValueError(f"Satuan dengan id {id} tidak ditemukan.")
        self._repo.hapus(id)

    def cari_by_id(self, id: int) -> Optional[DTOSatuan]:
        entity = self._repo.cari_by_id(id)
        if entity:
            return DTOSatuan(id=entity.id, nama=entity.nama)
        return None

    def semua(self) -> List[DTOSatuan]:
        entities = self._repo.cari_semua()
        return [DTOSatuan(id=e.id, nama=e.nama) for e in entities]
