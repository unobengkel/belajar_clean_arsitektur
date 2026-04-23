from typing import Optional, List
from domain.repository_interfaces.if_satuan_repository import ISatuanRepository
from domain.entities.entity_satuan import Satuan
from data.models.model_satuan import ModelSatuan


class RepoSatuan(ISatuanRepository):
    """Implementasi repository untuk Satuan menggunakan SQLite."""

    def __init__(self):
        self._model = ModelSatuan()

    def simpan(self, entity: Satuan) -> Satuan:
        return self._model.insert(entity)

    def update(self, entity: Satuan) -> Satuan:
        return self._model.update(entity)

    def hapus(self, id: int) -> None:
        self._model.delete(id)

    def cari_by_id(self, id: int) -> Optional[Satuan]:
        return self._model.find_by_id(id)

    def cari_semua(self) -> List[Satuan]:
        return self._model.find_all()

    def cari_by_nama(self, nama: str) -> Optional[Satuan]:
        return self._model.find_by_nama(nama)
