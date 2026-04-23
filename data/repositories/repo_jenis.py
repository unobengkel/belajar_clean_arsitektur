from typing import Optional, List
from domain.repository_interfaces.if_jenis_repository import IJenisRepository
from domain.entities.entity_jenis import Jenis
from data.models.model_jenis import ModelJenis


class RepoJenis(IJenisRepository):
    """Implementasi repository untuk Jenis menggunakan SQLite."""

    def __init__(self):
        self._model = ModelJenis()

    def simpan(self, entity: Jenis) -> Jenis:
        return self._model.insert(entity)

    def update(self, entity: Jenis) -> Jenis:
        return self._model.update(entity)

    def hapus(self, id: int) -> None:
        self._model.delete(id)

    def cari_by_id(self, id: int) -> Optional[Jenis]:
        return self._model.find_by_id(id)

    def cari_semua(self) -> List[Jenis]:
        return self._model.find_all()

    def cari_by_nama(self, nama: str) -> Optional[Jenis]:
        return self._model.find_by_nama(nama)
