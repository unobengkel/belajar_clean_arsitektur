from typing import Optional, List
from database import get_conn
from domain.entities.entity_stok import Stok


class ModelStok:
    """Model untuk operasi CRUD tabel stok di SQLite."""

    def __init__(self):
        self._table = "stok"

    def insert(self, entity: Stok) -> Stok:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO {self._table} (idbarang, jumlah, last_timeupdate) VALUES (?, ?, ?)",
                (entity.idbarang, entity.jumlah, entity.last_timeupdate),
            )
            entity.id = cursor.lastrowid
        return entity

    def update(self, entity: Stok) -> Stok:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"UPDATE {self._table} SET idbarang = ?, jumlah = ?, last_timeupdate = ? WHERE id = ?",
                (entity.idbarang, entity.jumlah, entity.last_timeupdate, entity.id),
            )
        return entity

    def delete(self, id: int) -> None:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {self._table} WHERE id = ?", (id,))

    def find_by_id(self, id: int) -> Optional[Stok]:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self._table} WHERE id = ?", (id,))
            row = cursor.fetchone()
        if row:
            return Stok(
                id=row["id"],
                idbarang=row["idbarang"],
                jumlah=row["jumlah"],
                last_timeupdate=row["last_timeupdate"],
            )
        return None

    def find_all(self) -> List[Stok]:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self._table} ORDER BY last_timeupdate DESC")
            rows = cursor.fetchall()
        return [
            Stok(
                id=row["id"],
                idbarang=row["idbarang"],
                jumlah=row["jumlah"],
                last_timeupdate=row["last_timeupdate"],
            )
            for row in rows
        ]

    def find_by_idbarang(self, idbarang: int) -> Optional[Stok]:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM {self._table} WHERE idbarang = ?", (idbarang,)
            )
            row = cursor.fetchone()
        if row:
            return Stok(
                id=row["id"],
                idbarang=row["idbarang"],
                jumlah=row["jumlah"],
                last_timeupdate=row["last_timeupdate"],
            )
        return None
