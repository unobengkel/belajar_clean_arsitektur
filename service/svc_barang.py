from typing import Optional, List
from domain.repository_interfaces.if_barang_repository import IBarangRepository
from domain.repository_interfaces.if_jenis_repository import IJenisRepository
from domain.repository_interfaces.if_merek_repository import IMerekRepository
from domain.repository_interfaces.if_satuan_repository import ISatuanRepository
from domain.entities.entity_barang import Barang
from data.dto.dto_barang import DTOBarang
from data.models.model_barang import ModelBarang
from database import get_connection


class SvcBarang:
    """Service / Use Case untuk Barang."""

    def __init__(
        self,
        repo: IBarangRepository,
        repo_jenis: IJenisRepository,
        repo_merek: IMerekRepository,
        repo_satuan: ISatuanRepository,
    ):
        self._repo = repo
        self._repo_jenis = repo_jenis
        self._repo_merek = repo_merek
        self._repo_satuan = repo_satuan

    def _ke_dto(self, entity: Barang) -> DTOBarang:
        """Mengubah entity Barang menjadi DTOBarang dengan informasi tambahan."""
        nama_jenis = None
        nama_merek = None
        nama_satuan = None

        jenis = self._repo_jenis.cari_by_id(entity.idjenis)
        if jenis:
            nama_jenis = jenis.nama

        merek = self._repo_merek.cari_by_id(entity.idmerek)
        if merek:
            nama_merek = merek.nama

        satuan = self._repo_satuan.cari_by_id(entity.idsatuan)
        if satuan:
            nama_satuan = satuan.nama

        return DTOBarang(
            id=entity.id,
            idjenis=entity.idjenis,
            idmerek=entity.idmerek,
            idsatuan=entity.idsatuan,
            nama=entity.nama,
            nama_jenis=nama_jenis,
            nama_merek=nama_merek,
            nama_satuan=nama_satuan,
        )

    def tambah(self, idjenis: int, idmerek: int, idsatuan: int, nama: str) -> DTOBarang:
        if not self._repo_jenis.cari_by_id(idjenis):
            raise ValueError(f"Jenis dengan id {idjenis} tidak ditemukan.")
        if not self._repo_merek.cari_by_id(idmerek):
            raise ValueError(f"Merek dengan id {idmerek} tidak ditemukan.")
        if not self._repo_satuan.cari_by_id(idsatuan):
            raise ValueError(f"Satuan dengan id {idsatuan} tidak ditemukan.")

        entity = Barang(id=0, idjenis=idjenis, idmerek=idmerek, idsatuan=idsatuan, nama=nama)
        hasil = self._repo.simpan(entity)
        return self._ke_dto(hasil)

    def ubah(self, id: int, idjenis: int, idmerek: int, idsatuan: int, nama: str) -> DTOBarang:
        existing = self._repo.cari_by_id(id)
        if not existing:
            raise ValueError(f"Barang dengan id {id} tidak ditemukan.")
        existing.idjenis = idjenis
        existing.idmerek = idmerek
        existing.idsatuan = idsatuan
        existing.nama = nama
        hasil = self._repo.update(existing)
        return self._ke_dto(hasil)

    def hapus(self, id: int) -> None:
        existing = self._repo.cari_by_id(id)
        if not existing:
            raise ValueError(f"Barang dengan id {id} tidak ditemukan.")
        self._repo.hapus(id)

    def cari_by_id(self, id: int) -> Optional[DTOBarang]:
        entity = self._repo.cari_by_id(id)
        if entity:
            return self._ke_dto(entity)
        return None

    def semua(self) -> List[DTOBarang]:
        entities = self._repo.cari_semua()
        return [self._ke_dto(e) for e in entities]

    def cari_by_nama(self, nama: str) -> List[DTOBarang]:
        entities = self._repo.cari_by_nama(nama)
        return [self._ke_dto(e) for e in entities]
