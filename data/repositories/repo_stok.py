from typing import Optional, List
from domain.repository_interfaces.if_stok_repository import IStokRepository
from domain.entities.entity_stok import Stok
from data.models.model_stok import ModelStok


class RepoStok(IStokRepository):
    """Implementasi repository untuk Stok menggunakan SQLite."""

    def __init__(self):
        self._model = ModelStok()

    def simpan(self, entity: Stok) -> Stok:
        return self._model.insert(entity)

    def update(self, entity: Stok) -> Stok:
        return self._model.update(entity)

    def hapus(self, id: int) -> None:
        self._model.delete(id)

    def cari_by_id(self, id: int) -> Optional[Stok]:
        return self._model.find_by_id(id)

    def cari_semua(self) -> List[Stok]:
        return self._model.find_all()

    def cari_by_idbarang(self, idbarang: int) -> Optional[Stok]:
        return self._model.find_by_idbarang(idbarang)
