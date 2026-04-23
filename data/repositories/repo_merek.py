from typing import Optional, List
from domain.repository_interfaces.if_merek_repository import IMerekRepository
from domain.entities.entity_merek import Merek
from data.models.model_merek import ModelMerek


class RepoMerek(IMerekRepository):
    """Implementasi repository untuk Merek menggunakan SQLite."""

    def __init__(self):
        self._model = ModelMerek()

    def simpan(self, entity: Merek) -> Merek:
        return self._model.insert(entity)

    def update(self, entity: Merek) -> Merek:
        return self._model.update(entity)

    def hapus(self, id: int) -> None:
        self._model.delete(id)

    def cari_by_id(self, id: int) -> Optional[Merek]:
        return self._model.find_by_id(id)

    def cari_semua(self) -> List[Merek]:
        return self._model.find_all()

    def cari_by_nama(self, nama: str) -> Optional[Merek]:
        return self._model.find_by_nama(nama)
