import sqlite3
import os
from contextlib import contextmanager
from typing import Optional, Generator

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(_BASE_DIR, "belajar_clean.db")


def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
    """Mendapatkan koneksi ke database SQLite."""
    conn = sqlite3.connect(db_path or DB_PATH, timeout=10, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


@contextmanager
def get_conn(db_path: Optional[str] = None) -> Generator[sqlite3.Connection, None, None]:
    """Context manager: auto-commit dan close koneksi."""
    conn = get_connection(db_path)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_database(db_path: Optional[str] = None):
    """Inisialisasi tabel-tabel database."""
    with get_conn(db_path) as conn:
        cursor = conn.cursor()
        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS jenis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT NOT NULL UNIQUE
            );

            CREATE TABLE IF NOT EXISTS merek (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT NOT NULL UNIQUE
            );

            CREATE TABLE IF NOT EXISTS satuan (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT NOT NULL UNIQUE
            );

            CREATE TABLE IF NOT EXISTS barang (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                idjenis INTEGER NOT NULL,
                idmerek INTEGER NOT NULL,
                idsatuan INTEGER NOT NULL,
                nama TEXT NOT NULL,
                FOREIGN KEY (idjenis) REFERENCES jenis(id) ON DELETE RESTRICT,
                FOREIGN KEY (idmerek) REFERENCES merek(id) ON DELETE RESTRICT,
                FOREIGN KEY (idsatuan) REFERENCES satuan(id) ON DELETE RESTRICT
            );

            CREATE TABLE IF NOT EXISTS stok (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                idbarang INTEGER NOT NULL,
                jumlah INTEGER NOT NULL DEFAULT 0,
                last_timeupdate TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
                FOREIGN KEY (idbarang) REFERENCES barang(id) ON DELETE CASCADE
            );
        """)
