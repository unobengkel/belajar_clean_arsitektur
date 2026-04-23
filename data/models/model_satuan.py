from typing import Optional, List
from database import get_conn
from domain.entities.entity_satuan import Satuan


class ModelSatuan:
    """Model untuk operasi CRUD tabel satuan di SQLite."""

    def __init__(self):
        self._table = "satuan"

    def insert(self, entity: Satuan) -> Satuan:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO {self._table} (nama) VALUES (?)",
                (entity.nama,),
            )
            entity.id = cursor.lastrowid
        return entity

    def update(self, entity: Satuan) -> Satuan:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"UPDATE {self._table} SET nama = ? WHERE id = ?",
                (entity.nama, entity.id),
            )
        return entity

    def delete(self, id: int) -> None:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {self._table} WHERE id = ?", (id,))

    def find_by_id(self, id: int) -> Optional[Satuan]:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self._table} WHERE id = ?", (id,))
            row = cursor.fetchone()
        if row:
            return Satuan(id=row["id"], nama=row["nama"])
        return None

    def find_all(self) -> List[Satuan]:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self._table} ORDER BY nama ASC")
            rows = cursor.fetchall()
        return [Satuan(id=row["id"], nama=row["nama"]) for row in rows]

    def find_by_nama(self, nama: str) -> Optional[Satuan]:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self._table} WHERE nama = ?", (nama,))
            row = cursor.fetchone()
        if row:
            return Satuan(id=row["id"], nama=row["nama"])
        return None
