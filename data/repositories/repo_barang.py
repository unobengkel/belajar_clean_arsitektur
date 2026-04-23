from typing import Optional, List
from domain.repository_interfaces.if_barang_repository import IBarangRepository
from domain.entities.entity_barang import Barang
from data.models.model_barang import ModelBarang


class RepoBarang(IBarangRepository):
    """Implementasi repository untuk Barang menggunakan SQLite."""

    def __init__(self):
        self._model = ModelBarang()

    def simpan(self, entity: Barang) -> Barang:
        return self._model.insert(entity)

    def update(self, entity: Barang) -> Barang:
        return self._model.update(entity)

    def hapus(self, id: int) -> None:
        self._model.delete(id)

    def cari_by_id(self, id: int) -> Optional[Barang]:
        return self._model.find_by_id(id)

    def cari_semua(self) -> List[Barang]:
        return self._model.find_all()

    def cari_by_nama(self, nama: str) -> List[Barang]:
        return self._model.find_by_nama(nama)

    def cari_by_idjenis(self, idjenis: int) -> List[Barang]:
        return self._model.find_by_idjenis(idjenis)

    def cari_by_idmerek(self, idmerek: int) -> List[Barang]:
        return self._model.find_by_idmerek(idmerek)
