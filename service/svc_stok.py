from typing import Optional, List
from datetime import datetime
from domain.repository_interfaces.if_stok_repository import IStokRepository
from domain.repository_interfaces.if_barang_repository import IBarangRepository
from domain.entities.entity_stok import Stok
from data.dto.dto_stok import DTOStok


class SvcStok:
    """Service / Use Case untuk Stok Barang."""

    def __init__(self, repo: IStokRepository, repo_barang: IBarangRepository):
        self._repo = repo
        self._repo_barang = repo_barang

    def _ke_dto(self, entity: Stok) -> DTOStok:
        nama_barang = ""
        barang = self._repo_barang.cari_by_id(entity.idbarang)
        if barang:
            nama_barang = barang.nama
        return DTOStok(
            id=entity.id,
            idbarang=entity.idbarang,
            jumlah=entity.jumlah,
            last_timeupdate=entity.last_timeupdate,
            nama_barang=nama_barang,
        )

    def tambah_stok(self, idbarang: int, jumlah: int) -> DTOStok:
        """Menambah stok barang (transaksi masuk)."""
        if not self._repo_barang.cari_by_id(idbarang):
            raise ValueError(f"Barang dengan id {idbarang} tidak ditemukan.")
        if jumlah <= 0:
            raise ValueError("Jumlah tambah stok harus lebih dari 0.")

        existing = self._repo.cari_by_idbarang(idbarang)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if existing:
            existing.jumlah += jumlah
            existing.last_timeupdate = now
            hasil = self._repo.update(existing)
        else:
            entity = Stok(id=0, idbarang=idbarang, jumlah=jumlah, last_timeupdate=now)
            hasil = self._repo.simpan(entity)

        return self._ke_dto(hasil)

    def kurangi_stok(self, idbarang: int, jumlah: int) -> DTOStok:
        """Mengurangi stok barang (transaksi keluar)."""
        existing = self._repo.cari_by_idbarang(idbarang)
        if not existing:
            raise ValueError(f"Stok untuk barang id {idbarang} belum ada.")
        if existing.jumlah < jumlah:
            raise ValueError(f"Stok tidak mencukupi. Stok saat ini: {existing.jumlah}")
        if jumlah <= 0:
            raise ValueError("Jumlah kurangi stok harus lebih dari 0.")

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        existing.jumlah -= jumlah
        existing.last_timeupdate = now
        hasil = self._repo.update(existing)
        return self._ke_dto(hasil)

    def lihat_stok(self, idbarang: int) -> Optional[DTOStok]:
        """Melihat stok barang tertentu."""
        entity = self._repo.cari_by_idbarang(idbarang)
        if entity:
            return self._ke_dto(entity)
        return None

    def semua_stok(self) -> List[DTOStok]:
        """Melihat semua stok barang."""
        entities = self._repo.cari_semua()
        return [self._ke_dto(e) for e in entities]
