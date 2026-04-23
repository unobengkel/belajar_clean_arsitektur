from typing import Optional, List
from database import get_conn
from domain.entities.entity_barang import Barang


class ModelBarang:
    """Model untuk operasi CRUD tabel barang di SQLite."""

    def __init__(self):
        self._table = "barang"

    def insert(self, entity: Barang) -> Barang:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO {self._table} (idjenis, idmerek, idsatuan, nama) VALUES (?, ?, ?, ?)",
                (entity.idjenis, entity.idmerek, entity.idsatuan, entity.nama),
            )
            entity.id = cursor.lastrowid
        return entity

    def update(self, entity: Barang) -> Barang:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"UPDATE {self._table} SET idjenis = ?, idmerek = ?, idsatuan = ?, nama = ? WHERE id = ?",
                (entity.idjenis, entity.idmerek, entity.idsatuan, entity.nama, entity.id),
            )
        return entity

    def delete(self, id: int) -> None:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {self._table} WHERE id = ?", (id,))

    def find_by_id(self, id: int) -> Optional[Barang]:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self._table} WHERE id = ?", (id,))
            row = cursor.fetchone()
        if row:
            return Barang(
                id=row["id"],
                idjenis=row["idjenis"],
                idmerek=row["idmerek"],
                idsatuan=row["idsatuan"],
                nama=row["nama"],
            )
        return None

    def find_all(self) -> List[Barang]:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self._table} ORDER BY nama ASC")
            rows = cursor.fetchall()
        return [
            Barang(
                id=row["id"],
                idjenis=row["idjenis"],
                idmerek=row["idmerek"],
                idsatuan=row["idsatuan"],
                nama=row["nama"],
            )
            for row in rows
        ]

    def find_by_nama(self, nama: str) -> List[Barang]:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM {self._table} WHERE nama LIKE ? ORDER BY nama ASC",
                (f"%{nama}%",),
            )
            rows = cursor.fetchall()
        return [
            Barang(
                id=row["id"],
                idjenis=row["idjenis"],
                idmerek=row["idmerek"],
                idsatuan=row["idsatuan"],
                nama=row["nama"],
            )
            for row in rows
        ]

    def find_by_idjenis(self, idjenis: int) -> List[Barang]:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM {self._table} WHERE idjenis = ? ORDER BY nama ASC",
                (idjenis,),
            )
            rows = cursor.fetchall()
        return [
            Barang(
                id=row["id"],
                idjenis=row["idjenis"],
                idmerek=row["idmerek"],
                idsatuan=row["idsatuan"],
                nama=row["nama"],
            )
            for row in rows
        ]

    def find_by_idmerek(self, idmerek: int) -> List[Barang]:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM {self._table} WHERE idmerek = ? ORDER BY nama ASC",
                (idmerek,),
            )
            rows = cursor.fetchall()
        return [
            Barang(
                id=row["id"],
                idjenis=row["idjenis"],
                idmerek=row["idmerek"],
                idsatuan=row["idsatuan"],
                nama=row["nama"],
            )
            for row in rows
        ]
